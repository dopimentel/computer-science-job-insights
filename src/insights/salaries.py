from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

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
                if job["max_salary"] != "" and job["max_salary"] != "invalid"
            ]
        )

    def get_min_salary(self) -> int:
        pass

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
