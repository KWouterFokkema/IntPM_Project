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
    makespan = ending_time(instance.machines[-1], job_order[-1])

    return starting_times, makespan, False


def visualize(instance, starting_times, optimal=False):
    """Creates a Gantt chart for the given instance and starting times"""
    assert all(
        (machine, job) in starting_times
        for machine in instance.machines
        for job in instance.jobs
    )

    makespan = round(
        max(
            starting_times[(instance.machines[-1], job)]
            + instance.processing_times[(instance.machines[-1], job)]
            for job in instance.jobs
        )
    )

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
    plt.savefig(fr"solutions\last\{instance.name}.png")
    if optimal:
        plt.savefig(fr"solutions\optimal\{instance.name}.png")

    plt.close()

