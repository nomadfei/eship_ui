import pytest
from selenium import webdriver

from page.shipping_calculate import ShippingCalculate


@pytest.fixture(scope="session")
def browser_driver(request):
    driver = webdriver.Chrome()  # 创建浏览器驱动
    request.addfinalizer(driver.quit)  # 在整个测试会话结束后执行driver.quit()
    yield driver


@pytest.fixture(scope="function")
def shipping_calculate_page(browser_driver):
    page = ShippingCalculate(browser_driver)
    browser_driver.get("https://www.easyship.com/shipping-rate-calculator/usa-to-usa")
    browser_driver.implicitly_wait(10)
    yield page
