import itertools
import gurobipy as gb
from util import draw_gantt


def add_starting_time_variables(model, instance):
    starting_times_vars = {}

    for machine in instance.machines:
        for job in instance.jobs:
            starting_times_vars[(machine, job)] = model.addVar(
                name=f"starting time ({machine}, {job})",
                lb=instance.minimal_preprocessing[(machine, job)]
            )
            starting_times_vars[(machine, job)].start = instance.best_solution[(machine, job)]

    return starting_times_vars


def add_ordering_variables(model, instance):
    ordering_vars = {}
    for machine in instance.machines[1:-1]:
        for (job_1, job_2) in itertools.combinations(instance.jobs, 2):
            order_var = model.addVar(
                name=f"order ({machine}, {job_1}, {job_2})",
                vtype=gb.GRB.BINARY
            )
            order_var.start = 1 if instance.best_solution[(machine, job_1)] < instance.best_solution[(machine, job_2)] else 0
            ordering_vars[(machine, job_1, job_2)] = order_var
            ordering_vars[(machine, job_2, job_1)] = 1 - order_var

    for (job_1, job_2) in itertools.combinations(instance.jobs, 2):
        ordering_vars[(instance.machines[0], job_1, job_2)] = ordering_vars[
            (instance.machines[1], job_1, job_2)
        ]
        ordering_vars[(instance.machines[0], job_2, job_1)] = ordering_vars[
            (instance.machines[1], job_2, job_1)
        ]
        ordering_vars[(instance.machines[-1], job_1, job_2)] = ordering_vars[
            (instance.machines[-2], job_1, job_2)
        ]
        ordering_vars[(instance.machines[-1], job_2, job_1)] = ordering_vars[
            (instance.machines[-2], job_2, job_1)
        ]

    return ordering_vars


def add_job_shop_constraints(model, instance, starting_times_vars):
    # The job can only start if the job is finished on the previous machine.
    for machine, previous_machine in zip(instance.machines[1:], instance.machines[:-1]):
        for job in instance.jobs:
            model.addConstr(
                starting_times_vars[(machine, job)]
                >= starting_times_vars[(previous_machine, job)]
                + instance.processing_times[(previous_machine, job)]
            )


def add_machine_schedule_indicator_constraints(model, instance, starting_times_vars, ordering_vars):
    for machine in instance.machines[1:-1]:
        for (job_1, job_2) in itertools.combinations(instance.jobs, 2):
            model.addConstr(
                (ordering_vars[(machine, job_1, job_2)] == 1)
                >> (
                        starting_times_vars[(machine, job_1)]
                        + instance.processing_times[(machine, job_1)]
                        <= starting_times_vars[(machine, job_2)]
                )
            )
            model.addConstr(
                (ordering_vars[(machine, job_1, job_2)] == 0)
                >> (
                        starting_times_vars[(machine, job_2)]
                        + instance.processing_times[(machine, job_2)]
                        <= starting_times_vars[(machine, job_1)]
                )
            )


def add_machine_schedule_big_m_constraints(model, instance, starting_times_vars, ordering_vars):
    for machine in instance.machines[1:-1]:
        for (job_1, job_2) in itertools.combinations(instance.jobs, 2):
            model.addConstr(
                starting_times_vars[(machine, job_1)]
                + instance.processing_times[(machine, job_1)]
                <= starting_times_vars[(machine, job_2)] + (1-ordering_vars[(machine, job_1, job_2)]) * instance.upper_bound
            )
            model.addConstr(
                starting_times_vars[(machine, job_2)]
                + instance.processing_times[(machine, job_2)]
                <= starting_times_vars[(machine, job_1)] + ordering_vars[(machine, job_1, job_2)] * instance.upper_bound
            )


def add_fixed_order_constraints(model, instance, ordering_vars):
    for (machine_1, machine_2) in zip(instance.machines[1:], instance.machines[:-1]):
        for (job_1, job_2) in itertools.combinations(instance.jobs, 2):
            model.addConstr(ordering_vars[(machine_1, job_1, job_2)] == ordering_vars[(machine_2, job_1, job_2)])


def add_starting_time_equalities(model, instance, starting_times_vars, ordering_vars, makespan_var):
    first_machine = instance.machines[0]
    for job in instance.jobs:
        model.addConstr(
            starting_times_vars[(first_machine, job)]
            == sum(
                ordering_vars[(first_machine, other_job, job)]
                * instance.processing_times[(first_machine, other_job)]
                for other_job in instance.jobs
                if other_job != job
            )
        )

    last_machine = instance.machines[-1]
    for job in instance.jobs:
        model.addConstr(
            starting_times_vars[(last_machine, job)]
            + instance.processing_times[(last_machine, job)]
            + sum(
                ordering_vars[(last_machine, job, other_job)]
                * instance.processing_times[(last_machine, other_job)]
                for other_job in instance.jobs
                if other_job != job
            )
            == makespan_var
        )


def retrieve_solution(instance, starting_times_vars):
    starting_times = {}

    for machine in instance.machines:
        for job in instance.jobs:
            starting_times[(machine, job)] = starting_times_vars[(machine, job)].x
    
    return starting_times


def get_cut_generator(instance, starting_times_vars, makespan_var):
    def cut_generator(model, where):
        if where != gb.GRB.Callback.MIPNODE:
            return
        if model.cbGet(gb.GRB.Callback.MIPNODE_NODCNT) != 0:
            return
        x = model.cbGetNodeRel(starting_times_vars)
        makespan_x = model.cbGetNodeRel(makespan_var)

        def g(machine_job_list, offset, mode):
            if mode == 'starting':
                sign = -1
            elif mode == 'completion':
                sign = 1
            else:
                raise ValueError
            processing_times_sum = sum(instance.processing_times[mj] for mj in machine_job_list)
            return (processing_times_sum**2
                    + sign * sum(instance.processing_times[mj]**2 for mj in machine_job_list)
                    )/2 + offset * processing_times_sum

        # Machine schedule cuts
        for machine in instance.machines:
            machine_order = sorted([(machine, job) for job in instance.jobs], key=x.__getitem__)
            worst_violation = 0
            worst_k = None
            starting_time_offset = None

            for k, machine_job in enumerate(machine_order):
                if starting_time_offset is None:
                    starting_time_offset = instance.minimal_preprocessing[machine_job]
                else:
                    starting_time_offset = min(starting_time_offset, instance.minimal_preprocessing[machine_job])

                violation = g(machine_order[:k+1], starting_time_offset, 'starting') - sum(instance.processing_times[mj] * x[mj] for mj in machine_order[:k+1])
                if violation > worst_violation:
                    worst_violation = violation
                    worst_k = k

            if round(worst_violation) > 0:
                # print(f"*Adding machine schedule cut for {worst_k+1} jobs on machine {machine}, {worst_violation=}*")
                model.cbCut(sum(starting_times_vars[mj] * instance.processing_times[mj] for mj in machine_order[:worst_k+1])
                            >=
                            g(machine_order[:worst_k+1], min(instance.minimal_preprocessing[mj] for mj in machine_order[:worst_k+1]), 'starting'))

        # Reverse machine schedule cuts
        for machine in instance.machines:
            machine_order = sorted([(machine, job) for job in instance.jobs], key=x.__getitem__, reverse=True)
            worst_violation = 0
            worst_k = None
            finishing_time_offset = None

            for k, machine_job in enumerate(machine_order):
                if finishing_time_offset is None:
                    finishing_time_offset = instance.minimal_postprocessing[machine_job]
                else:
                    finishing_time_offset = min(finishing_time_offset, instance.minimal_postprocessing[machine_job])

                violation = g(machine_order[:k+1], finishing_time_offset, 'completion') - sum(instance.processing_times[mj] * (makespan_x - x[mj]) for mj in machine_order[:k+1])
                if violation > worst_violation:
                    worst_violation = violation
                    worst_k = k

            if round(worst_violation) > 0:
                # print(f"*Adding reverse machine schedule cut for {worst_k+1} jobs on machine {machine}, {worst_violation=}*")
                model.cbCut(sum((makespan_var - starting_times_vars[mj]) * instance.processing_times[mj] for mj in machine_order[:worst_k+1])
                            >=
                            g(machine_order[:worst_k+1], min(instance.minimal_postprocessing[mj] for mj in machine_order[:worst_k+1]), 'completion'))

        # draw_gantt(instance, x, show=True)
    return cut_generator


# Solves the problem using binary ordering variables
def solve_ordering(instance, use_indicator=True, verbose=True, time_limit=10, fixed_order=False, use_cuts=False):
    model = gb.Model()

    makespan_var = model.addVar(obj=1, lb=instance.lower_bound or 0)
    starting_times_vars = add_starting_time_variables(model, instance)
    ordering_vars = add_ordering_variables(model, instance)

    add_job_shop_constraints(model, instance, starting_times_vars)

    if use_indicator:  # indicator constraints
        add_machine_schedule_indicator_constraints(model, instance, starting_times_vars, ordering_vars)
    else:  # Big-M constraints
        add_machine_schedule_big_m_constraints(model, instance, starting_times_vars, ordering_vars)

    add_starting_time_equalities(model, instance, starting_times_vars, ordering_vars, makespan_var)
    
    if fixed_order:
        add_fixed_order_constraints(model, instance, ordering_vars)

    if not verbose:
        model.setParam('LogToConsole', False)
    model.setParam("TimeLimit", time_limit)

    if use_cuts:
        model.setParam('PreCrush', False)
        cut_generator = get_cut_generator(instance, starting_times_vars, makespan_var)
        model.optimize(cut_generator)  # Solve the model with cutting plane callback
    else:
        model.optimize()  # Solve the model

    # Retrieve job starting times from the model
    solution = retrieve_solution(instance, starting_times_vars)
    upper_bound = round(model.ObjVal)

    if not instance.upper_bound or upper_bound < instance.upper_bound:
        instance.upper_bound = upper_bound
        instance.best_solution = solution

    if not fixed_order:
        lower_bound = round(model.ObjBound)
        if not instance.lower_bound or lower_bound > instance.lower_bound:
            instance.lower_bound = lower_bound

