import gurobipy as gb
import matplotlib.pyplot as plt
import sys
import re
import ast
import itertools


class Instance:
    def __init__(self, filename):
        name = filename.split('\\')[-1].replace('.py', '')
        print(f'Instance {name}')
        self.name = name

        with open(filename) as f:
            file_text = f.read()

        machines_text = re.search("machines = (.*)", file_text)[1]
        jobs_text = re.search("jobs = (.*)", file_text)[1]
        processing_times_text = re.search("processingTimes = (.*)", file_text)[1]

        self.machines = ast.literal_eval(machines_text)
        self.jobs = ast.literal_eval(jobs_text)
        self.processing_times = ast.literal_eval(processing_times_text)

    # This should probably be a separate function instead of a method
    # TODO: can these lower bounds be used to generate cutting planes?
    def print_lower_bounds(self):
        print('\nLower bounds:')

        for machine_nr, machine in enumerate(self.machines):
            def preprocessing_time(job):
                return sum(self.processing_times[(machine, job)] for machine in self.machines[:machine_nr])

            def postprocessing_time(job):
                return sum(self.processing_times[(machine, job)] for machine in self.machines[machine_nr+1:])

            minimal_preprocessing = min(preprocessing_time(job) for job in self.jobs)
            fastest_arriving_jobs = [job for job in self.jobs if preprocessing_time(job) == minimal_preprocessing]

            minimal_postprocessing = min(postprocessing_time(job) for job in self.jobs)
            fastest_leaving_jobs = [job for job in self.jobs if postprocessing_time(job) == minimal_postprocessing]

            machine_working_time = sum(self.processing_times[(machine, job)] for job in self.jobs)

            lower_bound = minimal_preprocessing + machine_working_time + minimal_postprocessing
            print(f'Machine {machine}: lower bound = {lower_bound}, first job in {fastest_arriving_jobs}, last job in {fastest_leaving_jobs}')
        print()

    def print_info(self):
        print(f'Machines: {len(self.machines)}')
        print(f'Jobs: {len(self.jobs)}')


# Solves the problem exactly using binary ordering variables
def solve(instance):
    model = gb.Model()

    makespan_var = model.addVar(obj=1)
    starting_times_vars = {}

    for machine in instance.machines:
        for job in instance.jobs:
            starting_times_vars[(machine, job)] = model.addVar(name=f"starting time ({machine}, {job})")

    # The job can only start if both the job and the machine are available.
    for machine, previous_machine in zip(instance.machines[1:], instance.machines[:-1]):
        for job in instance.jobs:
            model.addConstr(starting_times_vars[(machine, job)] >= starting_times_vars[(previous_machine, job)] + instance.processing_times[(previous_machine, job)])

    # Use the ordering variables with gurobi general constraints to enforce that jobs do not overlap
    # TODO: For the first and last machine, the inequalities could be rewritten to equalities which gives better LP bounds
    for machine in instance.machines:
        for (job_1, job_2) in itertools.combinations(instance.jobs, 2):
            order_var = model.addVar(name=f'order ({job_1}, {job_2})', vtype=gb.GRB.BINARY)
            model.addConstr((order_var == 1) >> (starting_times_vars[(machine, job_1)] + instance.processing_times[(machine, job_1)] <= starting_times_vars[(machine, job_2)]))
            model.addConstr((order_var == 0) >> (starting_times_vars[(machine, job_2)] + instance.processing_times[(machine, job_2)] <= starting_times_vars[(machine, job_1)]))

    # The makespan needs to be equal to the finishing time of the last job
    last_machine = instance.machines[-1]
    for job in instance.jobs:
        model.addConstr(makespan_var >= instance.processing_times[(last_machine, job)] + starting_times_vars[(last_machine, job)])

    model.setParam('TimeLimit', 100)
    model.optimize()  # Solve the model

    # Retrieve job starting times from the model
    starting_times = {}

    for machine in instance.machines:
        for job in instance.jobs:
            starting_times[(machine, job)] = starting_times_vars[(machine, job)].x

    return starting_times, model.Status == gb.GRB.OPTIMAL  # If the model is optimal, the solution is optimal


# Solves the scheduling problem assuming the permutation of the jobs does not change between machines
def solve_ordered(instance):
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

    model.setParam('TimeLimit', 10)
    model.optimize()  # Solve the model

    # Retrieve job starting times from the model
    starting_times = {}

    for machine in instance.machines:
        for job in instance.jobs:
            starting_times[(machine, job)] = sum(job_permutation_vars[(job, virtual_job)].x * virtual_starting_time_vars[(machine, virtual_job)].x for virtual_job in instance.jobs)

    return starting_times, False  # The second parameter is False because the solution is heuristic and not necessarily optimal


def basic_solution(instance, job_order=None):
    if job_order is None:
        job_order = instance.jobs[:]

    starting_times = {}

    def ending_time(machine, job):
        if (machine, job) in starting_times:
            return starting_times[(machine, job)] + instance.processing_times[(machine, job)]
        return 0

    for machine, previous_machine in zip(instance.machines, [None] + instance.machines):
        for job, previous_job in zip(job_order, [None] + job_order):
            machine_finished = 0 if previous_job is None else ending_time(machine, previous_job)
            job_finished = 0 if previous_machine is None else ending_time(previous_machine, job)
            starting_times[(machine, job)] = max(machine_finished, job_finished)

    print(f'Heuristic solution value: {ending_time(instance.machines[-1],job_order[-1])}')

    return starting_times, False


def visualize(instance, starting_times, optimal=False):
    assert (all((machine, job) in starting_times for machine in instance.machines for job in instance.jobs))

    color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

    fig, ax = plt.subplots(figsize=[6.4*2, 4.8])
    ax.invert_yaxis()
    machine_labels = [f'{machine}' for machine in instance.machines]

    for job in instance.jobs:
        job_labels = [f'{job}'] * len(instance.machines)
        job_widths = [instance.processing_times[(machine, job)] for machine in instance.machines]
        job_starts = [starting_times[(machine, job)] for machine in instance.machines]
        job_color = color_cycle[(job - 1) % len(color_cycle)]
        rects = ax.barh(machine_labels, job_widths, left=job_starts, color=job_color)
        text_color = 'black'
        ax.bar_label(rects, labels=job_labels, label_type='center', color=text_color)

    plt.xlabel('Time')
    plt.ylabel('Machines')
    plt.savefig(fr'solutions\last\{instance.name}.png')
    if optimal:
        plt.savefig(fr'solutions\optimal\{instance.name}.png')

    plt.close()


def main(input_path):
    instance = Instance(input_path)
    instance.print_lower_bounds()
    starting_times, optimal = solve(instance)
    visualize(instance, starting_times, optimal=optimal)


if __name__ == "__main__":
    main(sys.argv[1])
