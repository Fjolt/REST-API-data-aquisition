import requests
from typing import Dict, List
import os

CSV_FOLDER_NAME = 'csv_data' # Name of the directory with csv files.


# Gets users based on jobs they are assigned to.
def get_users(response: requests.Response) -> Dict[int, List[int]]:

    # Keys are user IDs and values are job IDs.
    users: Dict[int, List[int]] = {}
    users["Unassigned"] = []

    for res in response.json()["results"]:
        
        if res["assignee"]:
            if res["assignee"]["id"] in users.keys():
                users[res["assignee"]["id"]].append(res["id"])
            else:
                users[res["assignee"]["id"]] = [res["id"]]
            continue

        # If the job is unassigned, append him to the unassigned key
        users["Unassigned"].append(res["id"])

    
    # Prints count of all jobs (also those that are unassigned).
    print(len(response.json()["results"]))
    return users


# Gets basic information about jobs.
def get_jobs(response: requests.Response) -> Dict[int, tuple[str, str, str]]:    
    # Keys are task IDs and each job is assigned Status, State and Type
    jobs: Dict[int, tuple[str, str, str]] = {}

    for res in response.json()["results"]:
        jobs[res["id"]] = (res["status"], res["state"] ,res["type"])

    return jobs


# Exports data about given user to a csv file.
def create_csv(user_id: int, user_jobs: List[int], jobs: Dict[int, tuple[str, str, str]]) -> None:
    lines: List[str] = []

    lines.append(f'Jobs of the user {user_id} : \n')
    
    for i, job in enumerate(user_jobs):
        new_line = f'\nJob number {i + 1} :\n'+\
            f'    ID: {job},\n' +\
                f'    State: {jobs[job][0]},\n'+\
                    f'    Status: {jobs[job][1]},\n'+\
                        f'    Type: {jobs[job][2]},\n'
        lines.append(new_line)
    
    csv_file = os.path.join(CSV_FOLDER_NAME, f'user_{user_id}.csv')

    with open(csv_file, 'w', newline='') as file:
        for line in lines:
            file.write(line)


def main() -> None:
    # Getting the data from locally running server and printing the status code.
    response: requests.Response = requests.get("http://localhost:8080/api/jobs")
    print(response.status_code)

    # Printing the aquired data in json format.
    print(response.json())

    # Some data preparation
    users: Dict[int, List[int]] = get_users(response)
    jobs: Dict[int, tuple[str, str, str]] = get_jobs(response)

    # Create the folder if it doesn't exist
    if not os.path.exists(CSV_FOLDER_NAME):
        os.makedirs(CSV_FOLDER_NAME)
        print(f"Folder '{CSV_FOLDER_NAME}' created successfully.")
    
    # Iterates through users and creates a file for each of them.
    for user in users.keys():
        create_csv(user, users[user], jobs)


if __name__ == '__main__':
    main()