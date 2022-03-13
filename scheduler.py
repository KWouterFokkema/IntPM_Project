import sys

from instance import Instance
from algorithms.ordering import solve_ordering
from algorithms.permutation import solve_permutation
from johnson import johnson_meta
from util import visualize


def main(input_path):
    instance = Instance(input_path)
    solve_permutation(instance, verbose=False, fixed_order=True, use_indicator=True, use_cuts=False, time_limit=300)
    solve_ordering(instance, verbose=False, fixed_order=False, use_indicator=False, use_cuts=True, time_limit=300)
    print(instance.lower_bound, instance.upper_bound)

    visualize(instance)


if __name__ == "__main__":
    main(sys.argv[1])
