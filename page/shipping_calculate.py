from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.shipping_calculate_locator import ShippingCalculateLocators


class ShippingCalculate:
    def __init__(self, driver):
        self.driver = driver

    def submit_to_calculate(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, ShippingCalculateLocators.CALCULATE_SUBMIT_BUTTON))
        )

    def select_country(self, country):
        ship_from_dropdown = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.ID, ShippingCalculateLocators.SHIP_FROM_DROPDOWN))
        )
        ship_from_dropdown.click()

        country_selection_css = f"option[value={country}]"
        country_selection = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, country_selection_css))
        )
        country_selection.click()
        return country_selection

    def is_zip_code_displayed(self):
        try:
            self.driver.find_element(By.ID, ShippingCalculateLocators.ZIP_CODE_INPUT)
            return True
        except Exception:
            return False

    def set_parcel_weight(self, weight):
        parcel_weight_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.ID, ShippingCalculateLocators.PARCEL_WEIGHT_INPUT))
        )
        parcel_weight_element.clear()
        parcel_weight_element.send_keys(weight)
        actions = ActionChains(self.driver)
        actions.move_to_element(parcel_weight_element).perform()

    def click_on_refine_search_button(self):
        refine_search_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, ShippingCalculateLocators.REFINE_SEARCH_BUTTON))
        )
        refine_search_element.click()

    def parcel_weight_arrow_button_click(self, arrow_up=True):
        parcel_weight_arrow_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.ID, ShippingCalculateLocators.PARCEL_WEIGHT_INPUT))
        )
        parcel_weight_arrow_button.click()
        if arrow_up:
            parcel_weight_arrow_button.send_keys(Keys.ARROW_UP)
        else:
            parcel_weight_arrow_button.send_keys(Keys.ARROW_DOWN)
        parcel_weight_element_value = parcel_weight_arrow_button.get_attribute("value")
        return parcel_weight_element_value

    def select_weight_unit(self, weight_unit):
        weight_unit_dropdown = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.ID, ShippingCalculateLocators.WEIGHT_UNIT_DROPDOWN))
        )
        weight_unit_dropdown.click()

        weight_unit_selection_css = f"option[value={weight_unit}]"
        weight_unit_selection = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, weight_unit_selection_css))
        )
        weight_unit_selection.click()
        weight_unit_dropdown_value = weight_unit_dropdown.get_attribute("value")
        return weight_unit_dropdown_value

    def select_dimension_unit(self, dimension_unit):
        dimension_unit_dropdown = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, ShippingCalculateLocators.DIMENSION_UNIT_DROPDOWN))
        )
        dimension_unit_dropdown.click()

        dimension_unit_selection_css = f"option[value={dimension_unit}]"
        dimension_unit_selection = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, dimension_unit_selection_css))
        )
        dimension_unit_selection.click()
        dimension_unit_dropdown_value = dimension_unit_selection.get_attribute("value")
        return dimension_unit_dropdown_value

    def select_product_category(self, product_category):
        product_category_dropdown = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.ID, ShippingCalculateLocators.PRODUCT_CATEGORY_DROPDOWN))
        )
        product_category_dropdown.click()

        product_category_selection_css = f"option[value={product_category}]"
        product_category_selection = self.driver.find_element(By.CSS_SELECTOR, product_category_selection_css)
        product_category_selection.click()
        product_category_selection_value = product_category_selection.get_attribute("value")
        return product_category_selection_value
