# UI Automation using Pytest and Python

This repository is to give a working automation sample using a framework called Pytest for python. It runs tests against the page https://the-internet.herokuapp.com/ where it gives examples of different types of website interactions for a user.

# Why use Pytest?
Pytest is a Python-based test framework that is used to write and execute codes. It is mostly used for API testing but it is much more than that where you can write code for simple cases and more complex test cases. We can use Pytest to write API tests and besides we can code tests for database and UI tests.

* Pytest has its own way to detect the test file and test functions automatically, if not mentioned explicitly.
* It allows us to execute a specific part of a test suite and also skip a subset of the entire test suite.
* Pytest can run multiple tests in parallel, so it reduced the execution time of the test suite significantly.
* It has a simple syntax and is easy to learn and start using.
* It is open source and free.
* It has many documentation available and IDE support.
* Automatically support new browser versions

# How do I run tests?
Before running the test. Make sure to install all the required packages to the project
* pip install -r requirements. txt in your terminal

Navigate to root folder and run
* $ pytest --html=reports/report.html
* Default Browser is chrome
  * add --browser option to run a different browser e.g. --browser edge
* Browser Options:
  * chrome
  * edge
  * firefox
* To run specific marked tests
  * pytest --html=reports/report.html -m smoke

# How to run in parallel
  * use the -n option
    * -n auto
    * -n count e.g -n 3 will run 3 windows

# How to run in docker
  * Spin up an instance of the Selenium Grid in docker
    * This can be spun up using the docker-compose.yml file OR you can sping up Selenium Extensions in Docker Desktop
  * Options to run docker
    * --browser remote-chrome  : this will run in the chrome container
    * --browser remote-firefox : this will run in the firefox container
    * --browser remote-edge    : this will run in the edge container

# Explicit vs Implicit Waits
* Explicit wait will automatically retry if the condition returns false and until timeout expires 
  * e.g. WebDriverWait(driver, tieout=3).until(some_condition)
  * https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html
* Implicit will wait until a specific condition to occur
