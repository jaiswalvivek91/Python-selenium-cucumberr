from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class WaitUtils:
    def __init__(self, driver, default_timeout=10):
        self.driver = driver
        self.default_timeout = default_timeout

    @allure.step("Wait for element to be present: {locator}")
    def wait_for_element_present(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Element {locator} not present within {timeout} seconds")

    @allure.step("Wait for element to be visible: {locator}")
    def wait_for_element_visible(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Element {locator} not visible within {timeout} seconds")

    @allure.step("Wait for element to be clickable: {locator}")
    def wait_for_element_clickable(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Element {locator} not clickable within {timeout} seconds")

    @allure.step("Wait for text '{text}' to be present in element: {locator}")
    def wait_for_text_in_element(self, locator, text, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
        except TimeoutException:
            raise TimeoutException(f"Text '{text}' not present in {locator} within {timeout} seconds")

    @allure.step("Wait for URL to contain: {url_fragment}")
    def wait_for_url_contains(self, url_fragment, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.url_contains(url_fragment)
            )
        except TimeoutException:
            raise TimeoutException(f"URL does not contain '{url_fragment}' within {timeout} seconds")

    @allure.step("Wait for page title to contain: {title}")
    def wait_for_title_contains(self, title, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.title_contains(title)
            )
        except TimeoutException:
            raise TimeoutException(f"Page title does not contain '{title}' within {timeout} seconds")

    @allure.step("Wait for element to be invisible: {locator}")
    def wait_for_element_invisible(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Element {locator} still visible after {timeout} seconds")
