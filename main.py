import requests
from typing import Dict, List

# Gets users based on jobs they are assigned to.
def get_user_jobs(response: requests.Response) -> Dict[int, List[int]]:

    count = 0
    users: Dict[int, List[int]] = {}

    for res in response.json()["results"]:
        if res["assignee"]:
            if res["assignee"]["id"] in users.keys():
                users[res["assignee"]["id"]].append(res["task_id"])
            else:
                users[res["assignee"]["id"]] = res["task_id"]
        count += 1
    
    # Prints count of all jobs (also those that are unassigned).
    print(count)
    return users


def main() -> None:
    # Getting the data from locally running server and printing the status code.
    response = requests.get("http://localhost:8080/api/jobs")
    print(response.status_code)

    # Printing the aquired data in json format.
    print(response.json())

    # Some data preparation
    users = get_user_jobs(response)
    
    for user in users.keys():
        print(user, users[user])


if __name__ == '__main__':
    main()