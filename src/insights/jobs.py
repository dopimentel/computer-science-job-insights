import csv
from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # print (row['job_type'])
                self.jobs_list.append(dict(row))

    def get_unique_job_types(self) -> List[str]:
        return list(set([job['job_type'] for job in self.jobs_list]))

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass


process_jobs = ProcessJobs()
print(process_jobs.read("data/jobs.csv"))
print(process_jobs.get_unique_job_types())
