from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs

# from jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    @staticmethod
    def verify_key_in_job(job: Dict) -> bool:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError("Job must have min_salary and max_salary")

    def get_max_salary(self) -> int:
        # max_salary = 0
        # for job in self.jobs_list:
        #     if job["max_salary"] != "" and job["max_salary"] != "invalid":
        #         print(job["max_salary"])
        #         print(type(job["max_salary"]))
        #         if int(job["max_salary"]) > max_salary:
        #             max_salary = int(job["max_salary"])
        # return max_salary

        return max(
            [
                int(job["max_salary"])
                for job in self.jobs_list
                if job["max_salary"].isdigit()
            ]
        )

    def get_min_salary(self) -> int:
        return min(
            [
                int(job["min_salary"])
                for job in self.jobs_list
                if job["min_salary"].isdigit()
            ]
        )

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        ProcessSalaries.verify_key_in_job(job)
        try:
            # Convert values to integers
            min_salary = int(job["min_salary"])
            max_salary = int(job["max_salary"])

            if min_salary < 0:
                raise ValueError(
                    "Values of 'min_salary' and 'max_salary'"
                    "must be greater than or equal to zero."
                )

            # Check if min_salary is less than or equal to max_salary
            if min_salary >= max_salary:
                raise ValueError(
                    "'min_salary' must be less than or equal to 'max_salary'."
                )

            salary = int(salary)

            # Check if salary is within the salary range
            return min_salary <= salary <= max_salary
        except (ValueError, TypeError):
            raise ValueError(
                "Values of 'min_salary', 'max_salary',"
                "and 'salary' must be numeric."
            )

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass


process_salaries = ProcessSalaries()
# print(process_salaries.read("data/jobs.csv"))
print(
    process_salaries.matches_salary_range(
        {"max_salary": 1000, "min_salary": 100}, 100
    )
)
