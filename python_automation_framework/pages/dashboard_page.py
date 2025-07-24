"""
Dashboard page object
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class DashboardPage(BasePage):

    # Page locators
    PRODUCTS_CONTAINER = (By.CLASS_NAME, "inventory_container")
    WELCOME_MESSAGE = (By.CLASS_NAME, "app_logo")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")

    @allure.step("Check if dashboard is loaded")
    def is_dashboard_loaded(self):
        """Check if dashboard page is loaded by verifying products container"""
        return self.is_element_displayed(self.PRODUCTS_CONTAINER)

    @allure.step("Check if welcome message is displayed")
    def is_welcome_message_displayed(self):
        """Check if welcome message/logo is displayed"""
        return self.is_element_displayed(self.WELCOME_MESSAGE)

    @allure.step("Get welcome message text")
    def get_welcome_message(self):
        """Get the welcome message text"""
        return self.get_text(self.WELCOME_MESSAGE)

    @allure.step("Get product count")
    def get_product_count(self):
        """Get the number of products displayed"""
        products = self.find_elements(self.PRODUCT_ITEMS)
        return len(products)

    @allure.step("Click shopping cart")
    def click_shopping_cart(self):
        """Click on shopping cart icon"""
        self.click(self.SHOPPING_CART)

    @allure.step("Click menu button")
    def click_menu_button(self):
        """Click on hamburger menu button"""
        self.click(self.MENU_BUTTON)
