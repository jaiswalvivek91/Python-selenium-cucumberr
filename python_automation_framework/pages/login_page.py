# from selenium.webdriver.common.by import By
#
# class LoginPage:
#


"""
Login page object
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config_manager import ConfigManager
import allure
from utility.actions import GenericActions

class LoginPage(BasePage):

    # Page locators
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    LOGIN_CONTAINER = (By.CLASS_NAME, "login_container")

    def __init__(self, driver):
        super().__init__(driver)
        self.config_manager = ConfigManager()
        self.actions = GenericActions(driver)  # Initialize actions for element methods

    # URL = 'https://example.com/login'
    def load(self):
        # self.driver.get(self.URL)
        base_url = self.config_manager.get_base_url()
        login_url = f"{base_url}/login"
        self.navigate_to_url(login_url)

    def login(self, username, password):
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()

    def is_dashboard_displayed(self):
        return "dashboard" in self.driver.current_url

    @allure.step("Navigate to login page")
    def navigate_to_login(self):
        """Navigate to the login page"""
        base_url = self.config_manager.get_base_url()
        login_url = f"{base_url}/login"
        self.navigate_to_url(login_url)

    @allure.step("Enter username: {username}")
    def enter_username(self, username):
        """Enter username in the username field"""
        # self.enter_text(self.USERNAME_FIELD, username)
        self.actions.safe_send_keys(self.USERNAME_FIELD, username)

    @allure.step("Enter password")
    def enter_password(self, password):
        """Enter password in the password field"""
        # self.enter_text(self.PASSWORD_FIELD, password)
        self.actions.safe_send_keys(self.PASSWORD_FIELD, password)

    @allure.step("Click login button")
    def click_login(self):
        """Click the login button"""
        # self.click(self.LOGIN_BUTTON)
        self.actions.safe_click(self.LOGIN_BUTTON)

    @allure.step("Check if error message is displayed")
    def is_error_message_displayed(self):
        """Check if error message is displayed"""
        # return self.is_element_displayed(self.ERROR_MESSAGE)
        return self.actions.is_displayed(self.ERROR_MESSAGE)

    @allure.step("Get error message text")
    def get_error_message(self):
        """Get the error message text"""
        # return self.get_text(self.ERROR_MESSAGE)
        return self.actions.get_text(self.ERROR_MESSAGE)

    @allure.step("Check if login page is loaded")
    def is_login_page_loaded(self):
        """Check if login page is loaded"""
        # return self.is_element_displayed(self.LOGIN_CONTAINER)
        return self.actions.is_displayed(self.LOGIN_CONTAINER)

    @allure.step("Perform login with credentials")
    def login(self, username, password):
        """Perform complete login action"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
