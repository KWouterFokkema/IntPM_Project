import gurobipy as gb


# The following works, but is very slow.
def solve_permutation(instance):
    model = gb.Model()

    # Add variables to the model
    # We make a permutation of the jobs, called virtual_jobs.
    # On each machine, the first virtual_job is processed before the second, etc.

    job_permutation_vars = {}
    virtual_processing_time_vars = {}
    virtual_starting_time_vars = {}

    makespan_var = model.addVar(obj=1)

    for machine in instance.machines:
        for virtual_job in instance.jobs:
            for job in instance.jobs:
                job_permutation_vars[(machine, job, virtual_job)] = model.addVar(vtype=gb.GRB.BINARY)

    for machine in instance.machines:
        for virtual_job in instance.jobs:
            virtual_processing_time_vars[(machine, virtual_job)] = model.addVar()

    for machine in instance.machines:
        for virtual_job in instance.jobs:
            virtual_starting_time_vars[(machine, virtual_job)] = model.addVar()

    # Starting times in terms of original jobs
    starting_time_vars = {}
    for machine in instance.machines:
        for job in instance.jobs:
            starting_time_vars[(machine, job)] = model.addVar()

    model.update()

    for machine in instance.machines:
        for job in instance.jobs:
            for virtual_job in instance.jobs:
                model.addConstr((job_permutation_vars[(machine, job, virtual_job)] == 1) >> (starting_time_vars[(machine, job)] == virtual_starting_time_vars[(machine, virtual_job)]))

    # Permutation equalities
    for machine in instance.machines:
        for job in instance.jobs:
            model.addConstr(sum(job_permutation_vars[(machine, job, virtual_job)] for virtual_job in instance.jobs) == 1)
    for machine in instance.machines:
        for virtual_job in instance.jobs:
            model.addConstr(sum(job_permutation_vars[(machine, job, virtual_job)] for job in instance.jobs) == 1)

    # Processing time equalities
    for virtual_job in instance.jobs:
        for machine in instance.machines:
            model.addConstr(virtual_processing_time_vars[(machine, virtual_job)] == sum(job_permutation_vars[(machine, job, virtual_job)] * instance.processing_times[(machine, job)] for job in instance.jobs))

    # Starting time inequalities between jobs on the same machine
    for machine in instance.machines:
        for virtual_job, previous_virtual_job in zip(instance.jobs[1:], instance.jobs):
            if previous_virtual_job is None:
                continue
            model.addConstr(virtual_starting_time_vars[machine, virtual_job] >= virtual_starting_time_vars[machine, previous_virtual_job] + virtual_processing_time_vars[machine, previous_virtual_job])

    # Starting time inequalities between the same job on adjacent machines
    for machine, previous_machine in zip(instance.machines[1:], instance.machines):
        for job in instance.jobs:
            model.addConstr(starting_time_vars[(machine, job)] >= starting_time_vars[(previous_machine, job)] + instance.processing_times[(previous_machine, job)])

    # Order equations first two machines
    for virtual_job in instance.jobs:
        for job in instance.jobs:
            model.addConstr(job_permutation_vars[(instance.machines[0], job, virtual_job)] == job_permutation_vars[(instance.machines[1], job, virtual_job)])

    # Order equations last two machines
    for virtual_job in instance.jobs:
        for job in instance.jobs:
            model.addConstr(job_permutation_vars[(instance.machines[-2], job, virtual_job)] == job_permutation_vars[(instance.machines[-1], job, virtual_job)])

    # Starting time equations first and last machine
    for machine in (instance.machines[0], instance.machines[-1]):
        for virtual_job, previous_virtual_job in zip(instance.jobs[1:], instance.jobs):
            model.addConstr(virtual_starting_time_vars[(machine, virtual_job)] == virtual_starting_time_vars[(machine, previous_virtual_job)] + virtual_processing_time_vars[(machine, previous_virtual_job)])

    # Starting time equality
    model.addConstr(virtual_starting_time_vars[(instance.machines[0], instance.jobs[0])] == 0)

    # Makespan equality
    model.addConstr(makespan_var == virtual_starting_time_vars[(instance.machines[-1], instance.jobs[-1])] + virtual_processing_time_vars[(instance.machines[-1], instance.jobs[-1])])

    model.update()
    # model.setParam('LogToConsole', False)
    model.setParam('TimeLimit', 10)
    model.optimize()  # Solve the model
    # Retrieve job starting times from the model
    starting_times = {}

    for machine in instance.machines:
        for job in instance.jobs:
            starting_times[(machine, job)] = starting_time_vars[(machine, job)].getValue()

    return starting_times, makespan_var.x, model.Status == gb.GRB.OPTIMAL  # If the model is optimal, the solution is optimal


# Solves the scheduling problem assuming the permutation of the jobs does not change between machines
def solve_permutation_fixed(instance):
    model = gb.Model()

    # Add variables to the model
    # We make a permutation of the jobs, called virtual_jobs. The first virtual_job is processed before the second, etc.
    makespan_var = model.addVar(obj=1)
    job_permutation_vars = {}
    virtual_processing_time_vars = {}
    virtual_starting_time_vars = {}

    for job in instance.jobs:
        for virtual_job in instance.jobs:
            job_permutation_vars[(job, virtual_job)] = model.addVar(vtype=gb.GRB.BINARY)

    for virtual_job in instance.jobs:
        for machine in instance.machines:
            virtual_starting_time_vars[(machine, virtual_job)] = model.addVar()

    # Variables to model the processing times of virtual jobs
    for virtual_job in instance.jobs:
        for machine in instance.machines:
            virtual_processing_time_vars[(machine, virtual_job)] = model.addVar()

    # Add constraints to the model
    # These constraints could easily be combined, but perhaps gurobi recognizes similar constraints when they are added together?

    # Each job occurs once in the permutation
    for job in instance.jobs:
        model.addConstr(sum(job_permutation_vars[(job, virtual_job)] for virtual_job in instance.jobs) == 1)

    # Each virtual job occurs once in the permutation
    for virtual_job in instance.jobs:
        model.addConstr(sum(job_permutation_vars[(job, virtual_job)] for job in instance.jobs) == 1)

    # Constraints to model the processing times of virtual jobs
    for virtual_job in instance.jobs:
        for machine in instance.machines:
            model.addConstr(virtual_processing_time_vars[(machine, virtual_job)] == sum(job_permutation_vars[(job, virtual_job)] * instance.processing_times[(machine, job)] for job in instance.jobs))

    # For the first machine, the starting time is 0 or the finishing time of the previous job
    first_machine = instance.machines[0]
    for virtual_job, previous_job in zip(instance.jobs, [None] + instance.jobs):
        if previous_job is None:
            model.addConstr(virtual_starting_time_vars[(first_machine, virtual_job)] == 0)
        else:
            model.addConstr(virtual_starting_time_vars[(first_machine, virtual_job)] == virtual_starting_time_vars[(first_machine, previous_job)] + virtual_processing_time_vars[(first_machine, previous_job)])

    # For all other machines, the job can only start if both the job and the machine are available.
    for virtual_job, previous_job in zip(instance.jobs, [None] + instance.jobs):
        for machine, previous_machine in zip(instance.machines[1:], instance.machines):
            if previous_job is not None:
                model.addConstr(virtual_starting_time_vars[(machine, virtual_job)] >= virtual_starting_time_vars[(machine, previous_job)] + virtual_processing_time_vars[(machine, previous_job)])
            model.addConstr(virtual_starting_time_vars[(machine, virtual_job)] >= virtual_starting_time_vars[(previous_machine, virtual_job)] + virtual_processing_time_vars[(previous_machine, virtual_job)])

    # The makespan needs to be equal to the finishing time of the last virtual job
    last_machine = instance.machines[-1]
    last_virtual_job = instance.jobs[-1]

    model.addConstr(virtual_starting_time_vars[(last_machine, last_virtual_job)] + virtual_processing_time_vars[(last_machine, last_virtual_job)] <= makespan_var)

    # model.setParam('LogToConsole', False)
    model.setParam('TimeLimit', 10)
    model.optimize()  # Solve the model

    # Retrieve job starting times from the model
    starting_times = {}

    for machine in instance.machines:
        for job in instance.jobs:
            starting_times[(machine, job)] = sum(job_permutation_vars[(job, virtual_job)].x * virtual_starting_time_vars[(machine, virtual_job)].x for virtual_job in instance.jobs)

    # The second parameter is False because the solution is heuristic and not necessarily optimal
    return starting_times, makespan_var.x, round(model.objVal) == instance.get_lower_bound() 