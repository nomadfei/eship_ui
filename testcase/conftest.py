import pytest
from selenium import webdriver

from page.shipping_calculate import ShippingCalculate


@pytest.fixture(scope="session")
def browser_driver(request):
    # create driver
    driver = webdriver.Chrome()
    # close the driver after the session ends
    request.addfinalizer(driver.quit)
    yield driver


@pytest.fixture(scope="session")
def shipping_calculate_page(browser_driver):
    page = ShippingCalculate(browser_driver)
    # navigate to test page and wait for page loads
    browser_driver.get("https://www.easyship.com/shipping-rate-calculator/usa-to-usa")
    browser_driver.implicitly_wait(10)
    yield page


