from typing import Union, List, Dict

from src.insights.jobs import ProcessJobs

# from jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    @staticmethod
    def verify_mandatory_keys_in_job(job: Dict) -> None:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError("Job must have min_salary and max_salary")

    @staticmethod
    def verify_keys_values_in_job(job: Dict) -> bool:
        try:
            # Convert values to integers
            min_salary = int(job["min_salary"])
            max_salary = int(job["max_salary"])

        except (ValueError, TypeError):
            raise ValueError(
                "Values of 'min_salary' and 'max_salary'"
                "must be numeric, not empty, defined."
            )
        if min_salary < 0:
            raise ValueError(
                "Values of 'min_salary' and 'max_salary'"
                "must be greater than or equal to zero."
            )
        if min_salary > max_salary:
            raise ValueError(
                "'min_salary' must be less than or equal to 'max_salary'."
            )
        return True

    @staticmethod
    def verify_salary_is_numeric(salary: Union[str, int]) -> bool:
        if isinstance(salary, int):
            return True
        elif isinstance(salary, str) and salary.isdigit():
            return True
        else:
            raise ValueError("Salary must be numeric.")

    @staticmethod
    def compare(
        min_salary: Union[int, str],
        max_salary: Union[int, str],
        salary: Union[int, str],
    ) -> bool:

        return int(min_salary) <= int(salary) <= int(max_salary)

    def get_max_salaries_jobs(self) -> int:

        return [
            int(job["max_salary"])
            for job in self.jobs_list
            if job["max_salary"].isdigit()
        ]

    def get_max_salary(self) -> int:

        return max(self.get_max_salaries_jobs())

    def get_min_salaries_jobs(self) -> int:
        return [
            int(job["min_salary"])
            for job in self.jobs_list
            if job["min_salary"].isdigit()
        ]

    def get_min_salary(self) -> int:
        return min(self.get_min_salaries_jobs())

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        ProcessSalaries.verify_mandatory_keys_in_job(job)
        if ProcessSalaries.verify_keys_values_in_job(
            job
        ) and ProcessSalaries.verify_salary_is_numeric(salary):
            # Check if salary is within the salary range
            return ProcessSalaries.compare(
                job["min_salary"], job["max_salary"], salary
            )

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        valids_jobs = []
        for job in jobs:
            try:
                ProcessSalaries.verify_mandatory_keys_in_job(job)
                ProcessSalaries.verify_keys_values_in_job(job)
                ProcessSalaries.verify_salary_is_numeric(salary)
                if ProcessSalaries.compare(
                    job["min_salary"], job["max_salary"], salary
                ):
                    valids_jobs.append(job)
            except ValueError:
                pass
        # print(valids_jobs)

        return valids_jobs


# process_salaries = ProcessSalaries()
# # print(process_salaries.read("data/jobs.csv"))
# # print(
# #     process_salaries.matches_salary_range(
# #         {"max_salary": 1000, "min_salary": 100}, 100
# #     )
# # )

# list_of_jobs = [
#     {"max_salary": 1000},
#     {"min_salary": 1000},
#     {"max_salary": None, "min_salary": 1000},
#     {"max_salary": 0, "min_salary": 10},
#     {"max_salary": 10, "min_salary": 100},
#     {"max_salary": 10000, "min_salary": 200},
#     {"max_salary": 15000, "min_salary": 0},
#     {"max_salary": 1500, "min_salary": 0},
#     {"max_salary": -1, "min_salary": 10},
# ]


# process_salaries.filter_by_salary_range(list_of_jobs, 0)
