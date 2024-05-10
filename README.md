# Aquisition of data from CVAT REST API
Client-side script that obtains information about all jobs and exports them into csv files.

* Each user has their own csv files.
* Unassigned jobs can be found in "user_Unassigned.csv" file.
* Data is generated randomly.
* Runs test server locally using docker.
* Uses Python 3.10.1 and Docker image for the test server.

## Requirements

* Python 3.10.1 installed.
* Libraries: requests, typing, os, logging, unittest
* [Docker](https://www.docker.com/)

## Features implemented
* Obtaining of information and export to CSV. CSV files are located in the csv_data which is created if nonexistent.
* Logging using python logging library. The logs are written into logs.log file, which is automatically created after the first execution of the main.py program.
* Basic test suite in tests.py. Unit tests are used to test 3 main functions from main.py.

## Quick start

```bash
# Downloads a Docker image.
docker pull muonsoft/openapi-mock

# Runs a docker container with exported port 8080.
docker run -p 8080:8080 -e "OPENAPI_MOCK_SPECIFICATION_URL=https://app.cvat.ai/api/schema/" --rm muonsoft/openapi-mock

# Test that the server is running.
curl 'http://localhost:8080/api/jobs'

# Lastly try to run the python program to see the magic.
# Make sure you are in the correct directory before running.
python main.py
```