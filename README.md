# "OpenCart 3.0" UI test framework.

Frontend and backend testing. Product add to cart test. Admin create products test. Login and registration tests.

# Installation

To install the "OpenCart UI test framework" do the following.

1. Download it from repository: `git@github.com:denzel-commits/pythonQAESelenium.git`
2. Go to project folder: `cd pythonQAESelenium`
3. Create virtual environment: `python3 -m venv venv`
4. Activate virtual environment: `source venv/bin/activate`
5. You can install it now with the following command: `pip install -r requirements.txt`

This installs all modules required.


# Prerequisites

## Build OpenCart 3.0 test environment

Run this command for Windows:

   ``$Env:OPENCART_PORT=8081; $Env:PHPADMIN_PORT=8888; $Env:LOCAL_IP=$(Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias 'Wi-Fi' | Where-Object {$_.AddressFamily -eq 'IPv4'}).IPAddress; ./test_env/docker-compose up -d``


## Selenium Grid Standalone with Chrome
   ``docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:119.0``
   
Point executor to http://localhost:4444

# Running the Tests

192.168.1.127 is host local IP address

## Running locally:

``python3 -m pytest --base_url=http://192.168.1.127:8081``

## Running remotely in selenium grid:

``python3 -m pytest --base_url=http://192.168.1.127:8081 --executor=http://192.168.1.127:4444 --browser=chrome --bv=119.0``


## Running in Docker container:

1. Build docker image: ``docker build -t oc-ui-test .``
2. Run docker container: ``docker run --rm -it -v ${pwd}/allure-results:/usr/src/app/allure-results -v ${pwd}/logs/selenium:/usr/src/app/logs/selenium --name=running-ui-test oc-ui-test --executor=http://192.168.1.127:4444 --browser=chrome --bv="119.0"``

# Options

"Opencart UI test" accepts several options:

* --base_url: required option - specify opencart store url
* --executor: is optional, if specified tests will run remotely - remote executor URL
* --browser: is optional, browser name (chrome | firefox | safari), default=chrome
* --bv: is optional, is required if "executor" is specified - browser version
* --logging_level: is optional, log level (INFO | WARNING | ERROR)
* --headless: is optional, to run browser in headless mode

# Usage example
``python3 -m pytest --base_url=http://192.168.1.127:8081 --executor=http://192.168.1.127:4444 --browser=chrome --bv=119.0 --logging_level=INFO``

``python3 -m pytest -n=2 --base_url=http://192.168.1.127:8081 --executor=http://192.168.1.127:4444 --browser=chrome --bv=119.0 --logging_level=INFO``


# Running tests from Jenkins CI
Use "Jenkinsfile" to run the tests from Jenkins CI server

1. Create new Pipeline project
2. Choose Pipeline > Definition: Pipeline script from SCM
3. Set SCM to GIT
4. Set Repository URL: https://github.com/denzel-commits/pythonQAESelenium
5. Set Branches to build: "*/logger"
6. Script Path: "Jenkinsfile"
7. Click "Save"
8. Click "Build now with parameters" to start test run
9. Check allure report for results