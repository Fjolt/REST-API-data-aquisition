from typing import Dict, List
import os
import logging
from enum import Enum
import pandas as pd
import matplotlib.pyplot as plt

# User can switch between pretty formatting of the CSV file
# and formatting for later processing
class UseOfData(Enum):
    PRETTY = 1
    USEFUL = 2

PRETTY_CSV_FOLDER_NAME = 'csv_data_pretty'  # Name of the directory with pretty csv files.
CSV_FOLDER_NAME = 'csv_data_statistics'  # Name of the directory with csv files.


# Exports data in format chosen by thw user
def export_data(use: UseOfData, users: Dict[int, List[int]],\
                jobs: Dict[int, tuple[str, str, str]],
                graph_style: str="hist", col1: str = "Status", col2: str="frequency") -> None:
    if use == UseOfData.PRETTY:
        for user in users.keys():
            try:
                create_pretty_csv(user, users[user], jobs)
                logging.info(f"CSV file created for user: {user}.")
            except Exception as e:
                logging.error(f'Failed to create CSV file for user {user}')
                logging.error(f'{str(e)}')
        return

    csv_file = os.path.join(CSV_FOLDER_NAME, f'jobs.csv')

    # Creates the folder if it doesn't exist
    if not os.path.exists(csv_file):
        os.makedirs(CSV_FOLDER_NAME)
        logging.info(f"Folder '{CSV_FOLDER_NAME}' created successfully.")
        with open(csv_file, 'w', newline='') as file:
            file.write("")

    for user in users.keys():
        try:
            create_csv(user, users[user], jobs)
            logging.info(f"CSV lines added for user: {user}.")
        except Exception as e:
            logging.error(f'Failed to add lines for user {user}')
            logging.error(f'{str(e)}')

    compute_statistics(csv_file, 'Status', graph_style)


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

    lines: List[str] = []

    for i, job in enumerate(user_jobs):
        new_line = f'{user_id},{i + 1},{job},{jobs[job][0]},{jobs[job][1]},{jobs[job][2]}\n'
        lines.append(new_line)

    csv_file = os.path.join(CSV_FOLDER_NAME, f'jobs.csv')

    with open(csv_file, 'a', newline='') as file:
        file.writelines(lines)


def compute_statistics(csv_path: str, column1: str, graph_style:str):

    # Pandas reads the csv file and saves it to a dataframe.
    df = pd.read_csv(
        csv_path,
        header=0,
        names=['user_id', 'Job_number', 'ID', 'State', 'Status', 'Type']
    )

    plt.clf()

    value_counts = df[column1].value_counts()
    value_counts.plot(kind=graph_style)

    # Adda labels and title to the histogram.
    plt.xlabel(column1)
    plt.ylabel("Frequency")
    plt.title(f'{graph_style} plot of {column1}')

    plt.xticks(rotation=0)

    # Saves the plot to a histogram_state.png file in csv_data_statistics folder
    plt.savefig('csv_data_statistics/graph.png')

    print(df)