import sys

from instance import Instance
from algorithms.ordering import solve_ordering
from util import visualize


def main(input_path):
    instance = Instance(input_path)
    instance.print_lower_bounds()
    starting_times, makespan, optimal = solve_ordering(instance)
    visualize(instance, starting_times, optimal=optimal)


if __name__ == "__main__":
    main(sys.argv[1])
