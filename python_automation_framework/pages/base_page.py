"""
Base page class with common functionality for all pages
"""
from selenium.webdriver.support.ui import WebDriverWait
from utility.wait_utils import WaitUtils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(driver, 10)

    @allure.step("Navigate to URL: {url}")
    def navigate_to_url(self, url):
        """Navigate to target URL"""
        self.driver.get(url)

    @allure.step("Get current page URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Get page title")
    def get_page_title(self):
        return self.driver.title

    @allure.step("Close current browser tab")
    def close_browser(self):
        self.driver.close()

    @allure.step("Quit browser session")
    def quit_browser(self):
        self.driver.quit()

