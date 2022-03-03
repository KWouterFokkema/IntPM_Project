import re
import ast
from util import get_lower_bound


class Instance:
    def __init__(self, filename):
        name = filename.split("\\")[-1].replace(".py", "")
        self.name = name

        with open(filename) as f:
            file_text = f.read()

        machines_text = re.search("machines = (.*)", file_text)[1]
        jobs_text = re.search("jobs = (.*)", file_text)[1]
        processing_times_text = re.search("processingTimes = (.*)", file_text)[1]

        self.machines = ast.literal_eval(machines_text)
        self.jobs = ast.literal_eval(jobs_text)
        self.processing_times = ast.literal_eval(processing_times_text)
        self.lower_bound = get_lower_bound(self)
        self.upper_bound = None

    def print_info(self):
        print(f"Machines: {len(self.machines)}")
        print(f"Jobs: {len(self.jobs)}")

