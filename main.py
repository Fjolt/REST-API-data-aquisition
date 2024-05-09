import requests
from typing import Dict, List

# Gets users based on jobs they are assigned to.
def get_users(response: requests.Response) -> Dict[int, List[int]]:

    # Keys are user IDs and values are job IDs.
    users: Dict[int, List[int]] = {}
    users["unassigned"] = []

    for res in response.json()["results"]:
        
        if res["assignee"]:
            if res["assignee"]["id"] in users.keys():
                users[res["assignee"]["id"]].append(res["task_id"])
            else:
                users[res["assignee"]["id"]] = res["task_id"]
            continue

        # If the job is unassigned, append him to the unassigned key
        users["unassigned"].append(res["task_id"])

    
    # Prints count of all jobs (also those that are unassigned).
    print(len(response.json()["results"]))
    return users


# Gets basic information about jobs.
def get_jobs(response: requests.Response) -> Dict[int, tuple[str, str, str]]:    
    # Keys are task IDs and each job is assigned Status, State and Type
    jobs: Dict[int, tuple[str, str, str]] = {}

    for res in response.json()["results"]:
        jobs[res["task_id"]] = (res["status"], res["state"] ,res["type"])

    return jobs


def main() -> None:
    # Getting the data from locally running server and printing the status code.
    response: requests.Response = requests.get("http://localhost:8080/api/jobs")
    print(response.status_code)

    # Printing the aquired data in json format.
    print(response.json())

    # Some data preparation
    users: Dict[int, List[int]] = get_users(response)
    jobs: Dict[int, tuple[str, str, str]] = get_jobs(response)
    
    for user in users.keys():
        print(user, users[user])

    for job in jobs.keys():
        print(job, jobs[job])

if __name__ == '__main__':
    main()