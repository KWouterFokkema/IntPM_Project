import gurobipy as gb


def add_virtual_processing_time_vars(model, instance):
    virtual_processing_time_vars = {
        (machine, virtual_job): model.addVar()
        for virtual_job in instance.jobs
        for machine in instance.machines
    }

    return virtual_processing_time_vars


def add_virtual_starting_time_vars(model, instance):
    virtual_starting_time_vars = {
        (machine, virtual_job): model.addVar()
        for virtual_job in instance.jobs
        for machine in instance.machines
    }

    return virtual_starting_time_vars


def add_job_permutation_vars(model, instance):
    # Add variables to the model
    # We make a permutation of the jobs, called virtual_jobs.
    # On each machine, the first virtual_job is processed before the second, etc.

    job_permutation_vars = {}

    for machine in instance.machines[1:-1]:
        for virtual_job in instance.jobs:
            for job in instance.jobs:
                job_permutation_vars[(machine, job, virtual_job)] = model.addVar(
                    vtype=gb.GRB.BINARY
                )

    # Order equations first two and last two machines
    for virtual_job in instance.jobs:
        for job in instance.jobs:
            job_permutation_vars[(instance.machines[0], job, virtual_job)] = job_permutation_vars[(instance.machines[1], job, virtual_job)]
            job_permutation_vars[(instance.machines[-1], job, virtual_job)] = job_permutation_vars[(instance.machines[-2], job, virtual_job)]

    return job_permutation_vars


def add_fixed_job_permutation_vars(model, instance):
    fixed_job_permutation_vars = {}
    for virtual_job in instance.jobs:
        for job in instance.jobs:
            fixed_job_permutation_var = model.addVar(
                vtype=gb.GRB.BINARY
            )
            fixed_job_permutation_vars[(job, virtual_job)] = fixed_job_permutation_var

    return fixed_job_permutation_vars


def add_starting_time_variables(model, instance):
    # Starting times in terms of original jobs
    starting_time_vars = {}
    for machine in instance.machines:
        for job in instance.jobs:
            starting_time_vars[(machine, job)] = model.addVar()

    return starting_time_vars


def add_starting_time_indicator_constraints(model, instance, job_permutation_vars, virtual_starting_time_vars, starting_time_vars):
    for machine in instance.machines:
        for job in instance.jobs:
            for virtual_job in instance.jobs:
                model.addConstr(
                    (job_permutation_vars[(machine, job, virtual_job)] == 1)
                    >> (
                        starting_time_vars[(machine, job)]
                        == virtual_starting_time_vars[(machine, virtual_job)]
                    )
                )


def add_starting_time_big_m_constraints(model, instance, job_permutation_vars, virtual_starting_time_vars, starting_time_vars):
    for machine in instance.machines:
        for job in instance.jobs:
            for virtual_job in instance.jobs:
                model.addConstr(
                    starting_time_vars[(machine, job)]
                    <= virtual_starting_time_vars[(machine, virtual_job)]
                    + (1-job_permutation_vars[(machine, job, virtual_job)]) * instance.upper_bound
                )
                model.addConstr(
                    starting_time_vars[(machine, job)]
                    >= virtual_starting_time_vars[(machine, virtual_job)]
                    - (1-job_permutation_vars[(machine, job, virtual_job)]) * instance.upper_bound
                )


def add_fixed_job_permutation_constraints(model, instance, fixed_job_permutation_vars):
    for job in instance.jobs:
        model.addConstr(
            sum(
                fixed_job_permutation_vars[(job, virtual_job)]
                for virtual_job in instance.jobs
            )
            == 1
        )
    for virtual_job in instance.jobs:
        model.addConstr(
            sum(
                fixed_job_permutation_vars[(job, virtual_job)]
                for job in instance.jobs
            )
            == 1
        )


def add_job_permutation_constraints(model, instance, job_permutation_vars):
    for machine in instance.machines:
        for job in instance.jobs:
            model.addConstr(
                sum(
                    job_permutation_vars[(machine, job, virtual_job)]
                    for virtual_job in instance.jobs
                )
                == 1
            )
    for machine in instance.machines:
        for virtual_job in instance.jobs:
            model.addConstr(
                sum(
                    job_permutation_vars[(machine, job, virtual_job)]
                    for job in instance.jobs
                )
                == 1
            )


def add_processing_time_equalities(model, instance, virtual_processing_time_vars, job_permutation_vars):
    for virtual_job in instance.jobs:
        for machine in instance.machines:
            model.addConstr(
                virtual_processing_time_vars[(machine, virtual_job)]
                == sum(
                    job_permutation_vars[(machine, job, virtual_job)]
                    * instance.processing_times[(machine, job)]
                    for job in instance.jobs
                )
            )


def add_fixed_processing_time_equalities(model, instance, virtual_processing_time_vars, job_permutation_vars):
    for virtual_job in instance.jobs:
        for machine in instance.machines:
            model.addConstr(
                virtual_processing_time_vars[(machine, virtual_job)]
                == sum(
                    job_permutation_vars[(job, virtual_job)]
                    * instance.processing_times[(machine, job)]
                    for job in instance.jobs
                )
            )


def add_job_shop_constraints(model, instance, starting_time_vars):
    # Starting time inequalities between the same job on adjacent machines
    for machine, previous_machine in zip(instance.machines[1:], instance.machines[:-1]):
        for job in instance.jobs:
            model.addConstr(
                starting_time_vars[(machine, job)]
                >= starting_time_vars[(previous_machine, job)]
                + instance.processing_times[(previous_machine, job)]
            )


def add_virtual_job_shop_constraints(model, instance, virtual_starting_time_vars, job_permutation_vars):
    # Starting time inequalities between the same job on adjacent machines
    for machine, previous_machine in zip(instance.machines[1:], instance.machines[:-1]):
        for virtual_job in instance.jobs:
            model.addConstr(
                virtual_starting_time_vars[(machine, virtual_job)]
                >= virtual_starting_time_vars[(previous_machine, virtual_job)]
                + sum(instance.processing_times[(previous_machine, job)]*job_permutation_vars[(job, virtual_job)]
                      for job in instance.jobs)
            )

def add_machine_schedule_constraints(model, instance, virtual_starting_time_vars, virtual_processing_time_vars):
    # Starting time inequalities between jobs on the same machine
    for machine in instance.machines:
        for virtual_job, previous_virtual_job in zip(instance.jobs[1:], instance.jobs[:-1]):
            if previous_virtual_job is None:
                continue
            model.addConstr(
                virtual_starting_time_vars[machine, virtual_job]
                >= virtual_starting_time_vars[machine, previous_virtual_job]
                + virtual_processing_time_vars[machine, previous_virtual_job]
            )


def add_starting_time_equalities(model, instance, virtual_starting_time_vars, virtual_processing_time_vars):
    # Starting time equations first and last machine
    for machine in (instance.machines[0], instance.machines[-1]):
        for virtual_job, previous_virtual_job in zip(instance.jobs[1:], instance.jobs):
            model.addConstr(
                virtual_starting_time_vars[(machine, virtual_job)]
                == virtual_starting_time_vars[(machine, previous_virtual_job)]
                + virtual_processing_time_vars[(machine, previous_virtual_job)]
            )

    # Starting time equality
    model.addConstr(
        virtual_starting_time_vars[(instance.machines[0], instance.jobs[0])] == 0
    )


def add_makespan_equality(model, instance, virtual_starting_time_vars, virtual_processing_time_vars, makespan_var):
    # Makespan equality
    model.addConstr(
        makespan_var
        == virtual_starting_time_vars[(instance.machines[-1], instance.jobs[-1])]
        + virtual_processing_time_vars[(instance.machines[-1], instance.jobs[-1])]
    )


def retrieve_solution(instance, starting_time_vars):
    starting_times = {
        (machine, job): round(starting_time_vars[(machine, job)].x)
        for machine in instance.machines
        for job in instance.jobs
    }

    return starting_times


def retrieve_solution_fixed_order(instance, virtual_starting_time_vars, job_permutation_vars):
    starting_times = {
        (machine, job): round(sum(virtual_starting_time_vars[(machine, virtual_job)].x * job_permutation_vars[(job, virtual_job)].x
                                  for virtual_job in instance.jobs))
        for machine in instance.machines
        for job in instance.jobs
    }

    return starting_times


# Solves the problem using permutation variables
def solve_permutation(instance, verbose=True, use_indicator=True, time_limit=10, fixed_order=False, use_cuts=None):
    if fixed_order:
        return solve_permutation_fixed(instance, verbose=verbose, time_limit=time_limit)

    model = gb.Model()

    makespan_var = model.addVar(obj=1, lb=instance.lower_bound or 0)
    virtual_processing_time_vars = add_virtual_processing_time_vars(model, instance)
    virtual_starting_time_vars = add_virtual_starting_time_vars(model, instance)
    job_permutation_vars = add_job_permutation_vars(model, instance)
    starting_time_vars = add_starting_time_variables(model, instance)

    add_processing_time_equalities(model, instance, virtual_processing_time_vars, job_permutation_vars)
    add_starting_time_equalities(model, instance, virtual_starting_time_vars, virtual_processing_time_vars)
    add_makespan_equality(model, instance, virtual_starting_time_vars, virtual_processing_time_vars, makespan_var)

    if use_indicator:
        add_starting_time_indicator_constraints(model, instance, job_permutation_vars, virtual_starting_time_vars, starting_time_vars)
    else:
        add_starting_time_big_m_constraints(model, instance, job_permutation_vars, virtual_starting_time_vars, starting_time_vars)

    add_job_permutation_constraints(model, instance, job_permutation_vars)
    add_job_shop_constraints(model, instance, starting_time_vars)
    add_machine_schedule_constraints(model, instance, virtual_starting_time_vars, virtual_processing_time_vars)

    if not verbose:
        model.setParam('LogToConsole', False)
    model.setParam("TimeLimit", time_limit)
    model.optimize()  # Solve the model

    # Retrieve job starting times from the model
    solution = retrieve_solution(instance, starting_time_vars)
    upper_bound = round(model.ObjVal)
    lower_bound = round(model.ObjBound)

    if not instance.upper_bound or upper_bound < instance.upper_bound:
        instance.upper_bound = upper_bound
        instance.best_solution = solution

    if not instance.lower_bound or lower_bound > instance.lower_bound:
        instance.lower_bound = lower_bound


# Solves the scheduling problem assuming the permutation of the jobs does not change between machines
def solve_permutation_fixed(instance, verbose=True, time_limit=10):
    model = gb.Model()

    # Add variables to the model
    # We make a permutation of the jobs, called virtual_jobs. The first virtual_job is processed before the second, etc.
    makespan_var = model.addVar(obj=1)
    job_permutation_vars = add_fixed_job_permutation_vars(model, instance)
    virtual_processing_time_vars = add_virtual_processing_time_vars(model, instance)
    virtual_starting_time_vars = add_virtual_starting_time_vars(model, instance)

    add_starting_time_equalities(model, instance, virtual_starting_time_vars, virtual_processing_time_vars)
    add_fixed_processing_time_equalities(model, instance, virtual_processing_time_vars, job_permutation_vars)
    add_makespan_equality(model, instance, virtual_starting_time_vars, virtual_processing_time_vars, makespan_var)

    add_fixed_job_permutation_constraints(model, instance, job_permutation_vars)
    add_machine_schedule_constraints(model, instance, virtual_starting_time_vars, virtual_processing_time_vars)
    add_virtual_job_shop_constraints(model, instance, virtual_starting_time_vars, job_permutation_vars)

    if not verbose:
        model.setParam('LogToConsole', False)
    model.setParam("TimeLimit", time_limit)
    model.optimize()  # Solve the model

    # Retrieve job starting times from the model
    solution = retrieve_solution_fixed_order(instance, virtual_starting_time_vars, job_permutation_vars)
    upper_bound = round(model.ObjVal)

    if not instance.upper_bound or upper_bound < instance.upper_bound:
        instance.upper_bound = upper_bound
        instance.best_solution = solution
