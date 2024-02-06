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
        return list(set([job["job_type"] for job in self.jobs_list]))

    def filter_by_multiple_criteria(
        self, jobs: List[dict], filter_criteria: dict
    ) -> List[dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("filter_criteria must be a dictionary")
        jobs_filtered = jobs  # start with all jobs
        for criteria in filter_criteria.items():
            jobs_filtered = [
                job for job in jobs_filtered if job[criteria[0]] == criteria[1]
            ]
        return jobs_filtered


process_jobs = ProcessJobs()
print(process_jobs.read("data/jobs.csv"))
print(process_jobs.get_unique_job_types())


list_of_jobs = [
            {"max_salary": 15000, "min_salary": 0},
        {"max_salary": 1500, "min_salary": 0},
]
