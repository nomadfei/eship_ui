import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page.shipping_calculate import ShippingCalculate
import allure


@allure.feature("Shipping Calculate Feature")
class TestShippingCalculate:
    countries_data = [("spain", "Spain", False), ("usa", "United States", True)]
    weight_unit = ["kg", "lbs"]
    dimension_unit = ["cm", "in"]
    product_category = ["gaming", "accessory_no_battery"]

    @allure.story("Shipping From dropdown")
    @allure.description("Test the functionality of the Shipping From dropdown.")
    @pytest.mark.parametrize("country,selected_country_name,zip_code_displayed",
                             countries_data)
    @pytest.mark.priority("high")
    def test_shipping_from_dropdown(self, browser_driver, shipping_calculate_page, country, selected_country_name,
                                    zip_code_displayed):
        """
        Test case to:
        1. Ensure Shipping From dropdown is scrollable and it allows countries selection
        2. Verify Shipping From Zip Code filed is displayed when Shipping From is United States
        3. Verify Shipping From Zip Code filed is Not displayed when Shipping From is Not United States
        """
        selected_country_value = shipping_calculate_page.select_country(country).text

        assert selected_country_value == selected_country_name, "1. Verify the selected country is correct"
        assert shipping_calculate_page.is_zip_code_displayed() == zip_code_displayed, "2.Verify zip code displays, depending on different countries.Displayed for the United States. Not displayed for non-US countries"

    @allure.story("Parcel Weight Arrow button")
    @allure.description("Test the functionality of the Parcel Weight arrow button, including arrow up and arrow down.")
    @pytest.mark.priority("high")
    def test_parcel_weight_arrow_button(self, browser_driver, shipping_calculate_page):
        """
        Test case to:
        1. Verify that clicking the upward arrow increases the Parcel Weight by 0.01
        2. Verify that clicking the downward arrow decreases the Parcel Weight by 0.01
        """
        shipping_calculate_page.set_parcel_weight(99.99)
        parcel_weight_arrow_up_value = shipping_calculate_page.parcel_weight_arrow_button_click(arrow_up=True)
        assert parcel_weight_arrow_up_value == "100", "Parcel weight arrow up works"
        parcel_weight_arrow_down_value = shipping_calculate_page.parcel_weight_arrow_button_click(arrow_up=False)
        assert parcel_weight_arrow_down_value == "99.99", "Parcel weight arrow down works"


    @allure.story("Weight Unit dropdown")
    @allure.description("Test the functionality of the Weight Unit dropdown.")
    @pytest.mark.priority("high")
    @pytest.mark.parametrize("weight_unit",
                             weight_unit)
    def test_weight_unit_dropdown(self, browser_driver, shipping_calculate_page, weight_unit):
        weight_unit_value = shipping_calculate_page.select_weight_unit(weight_unit)
        """
        Test case to:
        1. Verify that the Weight Unit dropdown allows selection between lbs and kg and both options function correctly
        """
        assert weight_unit_value == weight_unit, "weight unit selection works"

    @allure.story("Dimension Unit dropdown")
    @allure.description("Test the functionality of the Dimension Unit dropdown.")
    @pytest.mark.priority("high")
    @pytest.mark.parametrize("dimension_unit",
                             dimension_unit)
    def test_dimension_unit_dropdown(self, browser_driver, shipping_calculate_page, dimension_unit):
        shipping_calculate_page.click_on_refine_search_button()
        """
        Test case to:
        1. Verify that the Dimensions Unit dropdown allows selection between in and cm and both options function correctly
        """
        dimension_unit_value = shipping_calculate_page.select_dimension_unit(dimension_unit)

        assert dimension_unit_value == dimension_unit, "dimension unit selection works"

    @allure.story("Product Category dropdown")
    @allure.description("Test the functionality of the Product Category dropdown.")
    @pytest.mark.priority("high")
    @pytest.mark.parametrize("product_category",
                             product_category)
    def test_product_category_dropdown(self, browser_driver, shipping_calculate_page, product_category):
        shipping_calculate_page.click_on_refine_search_button()
        """
        Test case to:
        1. Ensure Product Category dropdown is scrollable and it allows selection
        """
        product_category_value = shipping_calculate_page.select_product_category(product_category)

        assert product_category_value == product_category, "product category selection works"
