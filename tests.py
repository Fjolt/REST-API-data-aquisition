import unittest
from main import get_jobs, get_users, create_csv, CSV_FOLDER_NAME
import os

class MockResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data

class TestAPIScript(unittest.TestCase):

    def test_get_users(self):
        mock_response = MockResponse({
            "results": [
                {"id": 1, "assignee": {"id": 1}},
                {"id": 2, "assignee": None}
            ]
        })

        expected_result = {
            1: [1],
            "Unassigned": [2]
        }
        self.assertEqual(get_users(mock_response), expected_result)

    def test_get_jobs(self):
        mock_response = MockResponse({
            "results": [
                {"id": 1, "status": "validation", "state": "completed", "type": "annotation"},
                {"id": 2, "status": "validation", "state": "in progress", "type": "ground_truth"}
            ]
        })

        expected_result = {
            1: ("validation", "completed", "annotation"),
            2: ("validation", "in progress", "ground_truth")
        }
        self.assertEqual(get_jobs(mock_response), expected_result)

    def test_create_csv(self):
        user_id = -1
        user_jobs = [1, 2]
        jobs = {
            1: ("validation", "completed", "annotation"),
            2: ("validation", "in progress", "ground_truth")
        }

        if not os.path.exists(CSV_FOLDER_NAME):
            os.makedirs(CSV_FOLDER_NAME)

        create_csv(user_id, user_jobs, jobs)
        csv_file = os.path.join(CSV_FOLDER_NAME, f'user_{-1}.csv')
        self.assertEqual(os.path.exists(csv_file), True)

        expected_lines = [f'Jobs of the user {-1} : \n', '\n',\
                          f'Job number {1} :\n', f'    ID: {1},\n',\
                              f'    State: validation,\n',\
                               f'    Status: completed,\n', \
                                f'    Type: annotation,\n']

        expected_lines += ['\n',f'Job number {2} :\n', f'    ID: {2},\n',\
                              f'    State: validation,\n',\
                               f'    Status: in progress,\n', \
                                f'    Type: ground_truth,\n']

        with open(csv_file, 'r', newline='') as file:
            for line in expected_lines:
                self.assertEqual(file.readline(), line)


if __name__ == '__main__':
    unittest.main()