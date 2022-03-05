import matplotlib.pyplot as plt


# Heuristic using the given (or standard) job order
def basic_solution(instance, job_order=None):
    """Computes starting times and makespan for the given fixed job order"""
    if job_order is None:
        job_order = instance.jobs[:]

    starting_times = {}

    def ending_time(machine, job):
        if (machine, job) in starting_times:
            return (
                starting_times[(machine, job)]
                + instance.processing_times[(machine, job)]
            )
        return 0

    for machine, previous_machine in zip(instance.machines, [None] + instance.machines):
        for job, previous_job in zip(job_order, [None] + job_order):
            machine_finished = (
                0 if previous_job is None else ending_time(machine, previous_job)
            )
            job_finished = (
                0 if previous_machine is None else ending_time(previous_machine, job)
            )
            starting_times[(machine, job)] = max(machine_finished, job_finished)

    # print(f'Heuristic solution value: {ending_time(instance.machines[-1],job_order[-1])}')
    makespan = round(ending_time(instance.machines[-1], job_order[-1]))

    if instance.upper_bound is None or makespan < instance.upper_bound:
        instance.upper_bound = makespan
        instance.best_solution = starting_times


def draw_gantt(instance, starting_times, makespan=None, show=True):
    color_cycle = plt.rcParams["axes.prop_cycle"].by_key()["color"]

    fig, ax = plt.subplots(figsize=[6.4 * 2, 4.8])
    ax.invert_yaxis()
    machine_labels = [f"{machine}" for machine in instance.machines]

    for job in instance.jobs:
        job_labels = [f"{job}"] * len(instance.machines)
        job_widths = [
            instance.processing_times[(machine, job)] for machine in instance.machines
        ]
        job_starts = [starting_times[(machine, job)] for machine in instance.machines]
        job_color = color_cycle[(job - 1) % len(color_cycle)]
        rects = ax.barh(machine_labels, job_widths, left=job_starts, color=job_color)
        text_color = "black"
        ax.bar_label(rects, labels=job_labels, label_type="center", color=text_color)

    plt.xlabel("Time")
    plt.ylabel("Machines")
    plt.title(f"Makespan = {makespan}")
    if show:
        plt.show()


def visualize(instance):
    assert instance.best_solution
    starting_times = instance.best_solution
    makespan = instance.upper_bound

    """Creates a Gantt chart for the given instance and starting times"""
    assert all(
        (machine, job) in starting_times
        for machine in instance.machines
        for job in instance.jobs
    )

    draw_gantt(instance, starting_times, makespan, show=False)

    plt.savefig(fr"solutions\last\{instance.name}.png")

    if instance.lower_bound == instance.upper_bound:
        plt.savefig(fr"solutions\optimal\{instance.name}.png")

    plt.close()


# TODO: can these lower bounds be used to generate cutting planes?
def print_lower_bounds(instance):
    print("\nLower bounds:")

    for machine_nr, machine in enumerate(instance.machines):

        def preprocessing_time(job):
            return sum(
                instance.processing_times[(machine, job)]
                for machine in instance.machines[:machine_nr]
            )

        def postprocessing_time(job):
            return sum(
                instance.processing_times[(machine, job)]
                for machine in instance.machines[machine_nr + 1 :]
            )

        minimal_preprocessing = min(preprocessing_time(job) for job in instance.jobs)
        fastest_arriving_jobs = [
            job
            for job in instance.jobs
            if preprocessing_time(job) == minimal_preprocessing
        ]

        minimal_postprocessing = min(postprocessing_time(job) for job in instance.jobs)
        fastest_leaving_jobs = [
            job
            for job in instance.jobs
            if postprocessing_time(job) == minimal_postprocessing
        ]

        machine_working_time = sum(
            instance.processing_times[(machine, job)] for job in instance.jobs
        )

        lower_bound = (
            minimal_preprocessing + machine_working_time + minimal_postprocessing
        )
        print(
            f"Machine {machine}: lower bound = {lower_bound}, first job in {fastest_arriving_jobs}, last job in {fastest_leaving_jobs}"
        )
    print()


def get_lower_bound(instance):
    lower_bounds = []
    for machine_nr, machine in enumerate(instance.machines):

        def preprocessing_time(job):
            return sum(
                instance.processing_times[(machine, job)]
                for machine in instance.machines[:machine_nr]
            )

        def postprocessing_time(job):
            return sum(
                instance.processing_times[(machine, job)]
                for machine in instance.machines[machine_nr + 1 :]
            )

        minimal_preprocessing = min(preprocessing_time(job) for job in instance.jobs)
        fastest_arriving_jobs = [
            job
            for job in instance.jobs
            if preprocessing_time(job) == minimal_preprocessing
        ]

        minimal_postprocessing = min(postprocessing_time(job) for job in instance.jobs)
        fastest_leaving_jobs = [
            job
            for job in instance.jobs
            if postprocessing_time(job) == minimal_postprocessing
        ]

        machine_working_time = sum(
            instance.processing_times[(machine, job)] for job in instance.jobs
        )

        lower_bound = (
            minimal_preprocessing + machine_working_time + minimal_postprocessing
        )
        lower_bounds.append(lower_bound)

    return max(lower_bounds)
