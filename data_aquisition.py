import requests
from typing import Dict, List
import logging

# Where our local server is running.
SERVER_URL = 'http://localhost:8080/api/jobs'

def load_data() -> tuple[Dict[int, List[int]], Dict[int, tuple[str, str, str]]]:
    # Getting the data from locally running server and
    # printing the status code.
    response: requests.Response = requests.get(SERVER_URL)
    logging.info(f'Response Status Code: {response.status_code}')

    if (response.status_code != 200):
        logging.error(f'Unable to connect to {SERVER_URL}.')
        logging.info('Finishing application.')
        return

    # Prints response in json format in logs if DEBUG mode enbled.
    logging.debug(f"Response JSON Data:\n {response.json()}")

    # Some data preparation
    users: Dict[int, List[int]] = get_users(response)
    jobs: Dict[int, tuple[str, str, str]] = get_jobs(response)

    return(users,jobs)

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

    return users


# Gets basic information about jobs.
def get_jobs(response: requests.Response) -> Dict[int, tuple[str, str, str]]:
    # Keys are task IDs and each job is assigned Status, State and Type
    jobs: Dict[int, tuple[str, str, str]] = {}

    for res in response.json()["results"]:
        jobs[res["id"]] = (res["status"], res["state"], res["type"])

    return jobs