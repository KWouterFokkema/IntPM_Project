import re
import ast


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

    # This should probably be a separate function instead of a method
    # TODO: can these lower bounds be used to generate cutting planes?
    def print_lower_bounds(self):
        print("\nLower bounds:")

        for machine_nr, machine in enumerate(self.machines):

            def preprocessing_time(job):
                return sum(
                    self.processing_times[(machine, job)]
                    for machine in self.machines[:machine_nr]
                )

            def postprocessing_time(job):
                return sum(
                    self.processing_times[(machine, job)]
                    for machine in self.machines[machine_nr + 1 :]
                )

            minimal_preprocessing = min(preprocessing_time(job) for job in self.jobs)
            fastest_arriving_jobs = [
                job
                for job in self.jobs
                if preprocessing_time(job) == minimal_preprocessing
            ]

            minimal_postprocessing = min(postprocessing_time(job) for job in self.jobs)
            fastest_leaving_jobs = [
                job
                for job in self.jobs
                if postprocessing_time(job) == minimal_postprocessing
            ]

            machine_working_time = sum(
                self.processing_times[(machine, job)] for job in self.jobs
            )

            lower_bound = (
                minimal_preprocessing + machine_working_time + minimal_postprocessing
            )
            print(
                f"Machine {machine}: lower bound = {lower_bound}, first job in {fastest_arriving_jobs}, last job in {fastest_leaving_jobs}"
            )
        print()

    def get_lower_bound(self):
        lower_bounds = []
        for machine_nr, machine in enumerate(self.machines):

            def preprocessing_time(job):
                return sum(
                    self.processing_times[(machine, job)]
                    for machine in self.machines[:machine_nr]
                )

            def postprocessing_time(job):
                return sum(
                    self.processing_times[(machine, job)]
                    for machine in self.machines[machine_nr + 1 :]
                )

            minimal_preprocessing = min(preprocessing_time(job) for job in self.jobs)
            fastest_arriving_jobs = [
                job
                for job in self.jobs
                if preprocessing_time(job) == minimal_preprocessing
            ]

            minimal_postprocessing = min(postprocessing_time(job) for job in self.jobs)
            fastest_leaving_jobs = [
                job
                for job in self.jobs
                if postprocessing_time(job) == minimal_postprocessing
            ]

            machine_working_time = sum(
                self.processing_times[(machine, job)] for job in self.jobs
            )

            lower_bound = (
                minimal_preprocessing + machine_working_time + minimal_postprocessing
            )
            lower_bounds.append(lower_bound)

        return max(lower_bounds)

    def print_info(self):
        print(f"Machines: {len(self.machines)}")
        print(f"Jobs: {len(self.jobs)}")

