from collections import defaultdict

"""Implementation of Johnson's rule for m machines"""
def virtual_processing_times(processing_times, pivot=None, between=True):
    """processing_times: dict, key = (machine, job)"""
    # extract job names
    jobs = set([e[1] for e in processing_times.keys()])
    machines = set([e[0] for e in processing_times.keys()])
    num_machines = len(machines)

    if pivot is None:
        pivot = num_machines//2

    ps = defaultdict(int)

    for machine in range(pivot - int(not between)):
        for job in jobs:
            ps[(1, job)] += processing_times[(machine+1, job)]
    for machine in range(pivot+1, num_machines):
        for job in jobs:
            ps[(2, job)] += processing_times[(machine+1, job)]

    return ps


def johnson_heuristic(processing_times, pivot=None, between=True):
    ps = virtual_processing_times(processing_times, pivot=pivot, between=between)

    # change ps into a list of tuples (p, machine, job) and sort by p
    ps_tuples = sorted([(p, *k) for k, p in ps.items()])

    # keep track of which jobs have already been scheduled
    seen = set()

    schedule_head = []
    schedule_tail = []

    # compute johnson's rule w.r.t. virtual machines
    for (_, m, j) in ps_tuples:
        if m == 1 and j not in seen:
            schedule_head.append(j)
            seen.add(j)
        if m == 2 and j not in seen:
            schedule_tail.insert(0, j)
            seen.add(j)

    return schedule_head + schedule_tail


def permutation_to_order_vars(permutation):
    num_jobs = max(permutation)
    order_vars = [[0 for _ in range(num_jobs)] for _ in range(num_jobs)]

    for idx, j in enumerate(permutation):
        for jafter in permutation[idx:]:
            order_vars[j-1][jafter-1] = 1

    return order_vars

