from util import basic_solution
from collections import defaultdict

"""Implementation of Johnson's rule for m machines"""


def virtual_processing_times(instance, pivot=None, between=True):
    num_machines = len(instance.machines)

    if pivot is None:
        pivot = num_machines//2

    ps = defaultdict(int)

    for job in instance.jobs:
        ps[(1, job)] = sum(instance.processing_times[(machine + 1, job)]
                           for machine in range(pivot - int(not between))
                           )

        ps[(2, job)] = sum(instance.processing_times[(machine + 1, job)]
                           for machine in range(pivot+1, num_machines)
                           )

    return ps


def johnson_heuristic(instance, pivot=None, between=True):
    ps = virtual_processing_times(instance, pivot=pivot, between=between)

    # change ps into a list of tuples (p, machine, job) and sort by p
    ps_tuples = sorted([(p, *k) for k, p in ps.items()])

    # keep track of which jobs have already been scheduled
    seen = set()

    schedule_head = []
    schedule_tail_reversed = []

    # compute johnson's rule w.r.t. virtual machines
    for (_, m, j) in ps_tuples:
        if j in seen:
            continue

        if m == 1:
            schedule_head.append(j)
        elif m == 2:
            schedule_tail_reversed.append(j)

        seen.add(j)

    return schedule_head + list(reversed(schedule_tail_reversed))


def johnson_heuristic_meta(instance):
    schedules = []
    for flag in [True, False]:
        for pivot in range(1, len(instance.machines)+1):
            schedules.append(johnson_heuristic(instance, pivot=pivot, between=flag))
    return schedules


def permutation_to_order_vars(permutation):
    num_jobs = max(permutation)
    order_vars = [[0 for _ in range(num_jobs)] for _ in range(num_jobs)]

    for idx, j in enumerate(permutation):
        for jafter in permutation[idx:]:
            order_vars[j-1][jafter-1] = 1

    return order_vars


def johnson_meta(instance):
    permutations = johnson_heuristic_meta(instance)
    # get best permutation
    makespans = [basic_solution(instance, job_order=p)[1] for p in permutations]
    best = makespans.index(min(makespans))
    permutation = permutations[best]
    basic_solution(instance, job_order=permutation)
    # ordering_vars_johnson = permutation_to_order_vars(permutation)

