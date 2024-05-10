from typing import Dict, List
import os
import logging
from enum import Enum

# User can switch between pretty formatting of the CSV file
# and formatting for later processing
class UseOfData(Enum):
    PRETTY = 1
    USEFUL = 2

PRETTY_CSV_FOLDER_NAME = 'csv_data_pretty'  # Name of the directory with pretty csv files.
CSV_FOLDER_NAME = 'csv_data'  # Name of the directory with csv files.

# Exports data in format chosen by thw user
def export_data(use: UseOfData, users: Dict[int, List[int]],\
                jobs: Dict[int, tuple[str, str, str]]) -> None:
    if use == UseOfData.PRETTY:
        for user in users.keys():
            try:
                create_pretty_csv(user, users[user], jobs)
                logging.info(f"CSV file created for user: {user}.")
            except Exception as e:
                logging.error(f'Failed to create CSV file for user {user}')
                logging.error(f'{str(e)}')
        return


# Exports data about given user to a csv file in a human readable format.
def create_pretty_csv(user_id: int, user_jobs: List[int],
               jobs: Dict[int, tuple[str, str, str]]) -> None:

    # Creates the folder if it doesn't exist
    if not os.path.exists(PRETTY_CSV_FOLDER_NAME):
        os.makedirs(PRETTY_CSV_FOLDER_NAME)
        logging.info(f"Folder '{PRETTY_CSV_FOLDER_NAME}' created successfully.")

    lines: List[str] = []

    lines.append(f'Jobs of the user {user_id} : \n')

    for i, job in enumerate(user_jobs):
        new_line = f'\nJob number {i + 1} :\n' + \
            f'    ID: {job},\n' + \
            f'    State: {jobs[job][0]},\n' + \
            f'    Status: {jobs[job][1]},\n' + \
            f'    Type: {jobs[job][2]},\n'
        lines.append(new_line)

    csv_file = os.path.join(PRETTY_CSV_FOLDER_NAME, f'user_{user_id}.csv')

    with open(csv_file, 'w', newline='') as file:
        for line in lines:
            file.write(line)

# Exports data about given user to a csv file in a computer friendly format.
def create_csv(user_id: int, user_jobs: List[int],
               jobs: Dict[int, tuple[str, str, str]]) -> None:

    # Creates the folder if it doesn't exist
    if not os.path.exists(CSV_FOLDER_NAME):
        os.makedirs(CSV_FOLDER_NAME)
        logging.info(f"Folder '{CSV_FOLDER_NAME}' created successfully.")

    lines: List[str] = []

    lines.append(f'Jobs of the user {user_id} : \n')

    for i, job in enumerate(user_jobs):
        new_line = f'\nJob number {i + 1} :\n' + \
            f'    ID: {job},\n' + \
            f'    State: {jobs[job][0]},\n' + \
            f'    Status: {jobs[job][1]},\n' + \
            f'    Type: {jobs[job][2]},\n'
        lines.append(new_line)

    csv_file = os.path.join(PRETTY_CSV_FOLDER_NAME, f'user_{user_id}.csv')

    with open(csv_file, 'w', newline='') as file:
        for line in lines:
            file.write(line)
