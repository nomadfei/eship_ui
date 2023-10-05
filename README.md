# UI Automation
UI Automation for Easy Ship. 
Currently, only Chrome browser is supported. Other browsers will be supported in the future.

## Prerequisites
- Python 3.x installed
- Pip installed
- Google Chrome browser installed
- Allure installed

## Installation
Install pytest
```commandline
pip install pytest
```
Install Selenium
```commandline
pip install selenium
```
Install allure-pytest
```commandline
pip install allure-pytest
```
Selenium Webdriver
- Download Chromedriver
- Add it to your PATH variable.

## Run tests
Go to the project
```
cd project
```
Run the tests
```commandline
pytest ./testcase/test_shipping_calculate.py --alluredir ./test_result --clean-alluredir
```
Generate and view test result
```commandline
allure serve ./test_result
```