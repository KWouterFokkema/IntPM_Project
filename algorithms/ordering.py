import itertools
import gurobipy as gb


# Solves the problem exactly using binary ordering variables
def solve_ordering(instance):
    use_indicator = True
    model = gb.Model()

    makespan_var = model.addVar(obj=1)
    starting_times_vars = {}

    for machine in instance.machines:
        for job in instance.jobs:
            starting_times_vars[(machine, job)] = model.addVar(
                name=f"starting time ({machine}, {job})"
            )

    # The job can only start if the job is finished on the previous machine.
    for machine, previous_machine in zip(instance.machines[1:], instance.machines[:-1]):
        for job in instance.jobs:
            model.addConstr(
                starting_times_vars[(machine, job)]
                >= starting_times_vars[(previous_machine, job)]
                + instance.processing_times[(previous_machine, job)]
            )

    # Use the ordering variables with gurobi general constraints to enforce that jobs do not overlap
    order_vars = {}
    for machine in instance.machines[1:-1]:
        for (job_1, job_2) in itertools.combinations(instance.jobs, 2):
            order_var = model.addVar(
                name=f"order ({machine}, {job_1}, {job_2})", vtype=gb.GRB.BINARY
            )
            order_vars[(machine, job_1, job_2)] = order_var
            order_vars[(machine, job_2, job_1)] = 1 - order_var
            if use_indicator:
                model.addConstr(
                    (order_var == 1)
                    >> (
                        starting_times_vars[(machine, job_1)]
                        + instance.processing_times[(machine, job_1)]
                        <= starting_times_vars[(machine, job_2)]
                    )
                )
                model.addConstr(
                    (order_var == 0)
                    >> (
                        starting_times_vars[(machine, job_2)]
                        + instance.processing_times[(machine, job_2)]
                        <= starting_times_vars[(machine, job_1)]
                    )
                )
            else:
                pass
                # model.addConstr(starting_times_vars[(machine, job_1)] + instance.processing_times[(machine, job_1)] <= starting_times_vars[(machine, job_2)] + M * )
                # model.addConstr(starting_times_vars[(machine, job_2)] + instance.processing_times[(machine, job_2)] <= starting_times_vars[(machine, job_1)] + M * )

    for (job_1, job_2) in itertools.combinations(instance.jobs, 2):
        order_vars[(instance.machines[0], job_1, job_2)] = order_vars[
            (instance.machines[1], job_1, job_2)
        ]
        order_vars[(instance.machines[0], job_2, job_1)] = order_vars[
            (instance.machines[1], job_2, job_1)
        ]
        order_vars[(instance.machines[-1], job_1, job_2)] = order_vars[
            (instance.machines[-2], job_1, job_2)
        ]
        order_vars[(instance.machines[-1], job_2, job_1)] = order_vars[
            (instance.machines[-2], job_2, job_1)
        ]

    first_machine = instance.machines[0]
    for job in instance.jobs:
        model.addConstr(
            starting_times_vars[(first_machine, job)]
            == sum(
                order_vars[(first_machine, other_job, job)]
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
                order_vars[(last_machine, job, other_job)]
                * instance.processing_times[(last_machine, other_job)]
                for other_job in instance.jobs
                if other_job != job
            )
            == makespan_var
        )

    # The makespan needs to be equal to the finishing time of the last job
    last_machine = instance.machines[-1]
    for job in instance.jobs:
        model.addConstr(
            makespan_var
            >= instance.processing_times[(last_machine, job)]
            + starting_times_vars[(last_machine, job)]
        )

    # Lower bound constraint
    model.addConstr(makespan_var >= instance.get_lower_bound())

    # model.setParam('LogToConsole', False)
    model.setParam("TimeLimit", 10)
    model.optimize()  # Solve the model

    # Retrieve job starting times from the model
    starting_times = {}

    # TODO: add cutting planes

    for machine in instance.machines:
        for job in instance.jobs:
            starting_times[(machine, job)] = starting_times_vars[(machine, job)].x

    # If the model is optimal, the solution is optimal
    return starting_times, round(makespan_var.x), model.Status == gb.GRB.OPTIMAL

