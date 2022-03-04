import sys

from instance import Instance
from algorithms.ordering import solve_ordering
from algorithms.permutation import solve_permutation
from util import visualize


def main(input_path):
    instance = Instance(input_path)
    solve_ordering(instance, verbose=False, fixed_order=True)
    print(instance.upper_bound)
    visualize(instance)


if __name__ == "__main__":
    main(sys.argv[1])
