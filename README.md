# Aquisition of data from CVAT REST API
Client-side script that obtains information about all jobs and exports them into csv files.

* Each user has their own csv files.
* Unassigned jobs can be found in "user_Unassigned.csv" file.
* Data is generated randomly.
* Runs test server locally using docker.
* Uses Python 3.10.1 and Docker image for the test server.

## Requirements

* Python 3.10.1 installed.
* Libraries: requests, typing
* [Docker](https://www.docker.com/)

## Quick start

```bash
# Downloads a Docker image.
docker pull muonsoft/openapi-mock

# Runs a docker container with exported port 8080.
docker run -p 8080:8080 -e "OPENAPI_MOCK_SPECIFICATION_URL=https://app.cvat.ai/api/schema/" --rm muonsoft/openapi-mock

# Test that the server is running.
curl 'http://localhost:8080/api/jobs'
```