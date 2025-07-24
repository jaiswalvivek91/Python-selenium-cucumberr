"""
GenericActions: Common UI interactions, waits, dropdowns, etc.
"""

import time
import allure
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utility.wait_utils import WaitUtils
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class GenericActions:
    def __init__(self, driver, default_timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, default_timeout)
        self.timeout = default_timeout
        self.actions = ActionChains(driver)

    # Waits

    @allure.step("Wait for element to be present: {locator}")
    def wait_for_element_present(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Wait for element to be visible: {locator}")
    def wait_for_element_visible(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Wait for element to be clickable: {locator}")
    def wait_for_element_clickable(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Wait for text '{text}' in element: {locator}")
    def wait_for_text_in_element(self, locator, text, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    @allure.step("Wait for element to disappear: {locator}")
    def wait_for_element_invisible(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Wait for page title to contain: {title}")
    def wait_for_title_contains(self, title, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.title_contains(title)
        )

    @allure.step("Wait for URL to contain: {url_fragment}")
    def wait_for_url_contains(self, url_fragment, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.url_contains(url_fragment)
        )

    # Element Actions

    @allure.step("Click element: {locator}")
    def safe_click(self, locator, timeout=None, retries=3):
        timeout = timeout or self.timeout
        for attempt in range(retries):
            try:
                element = self.wait_for_element_clickable(locator, timeout)
                element.click()
                return
            except Exception as e:
                if attempt == retries - 1:
                    allure.attach(str(e), name="Click Error", attachment_type=allure.attachment_type.TEXT)
                    raise Exception(f"Failed to click {locator}: {str(e)}")
                time.sleep(1)

    @allure.step("Send keys '{text}' to element: {locator}")
    def safe_send_keys(self, locator, text, clear_first=True, timeout=None, retries=3):
        timeout = timeout or self.timeout
        for attempt in range(retries):
            try:
                element = self.wait_for_element_visible(locator, timeout)
                if clear_first:
                    element.clear()
                element.send_keys(text)
                return
            except Exception as e:
                if attempt == retries - 1:
                    allure.attach(str(e), name="Send Keys Error", attachment_type=allure.attachment_type.TEXT)
                    raise Exception(f"Failed to send keys to {locator}: {str(e)}")
                time.sleep(1)

    @allure.step("Get text from element: {locator}")
    def get_text(self, locator, timeout=None):
        element = self.wait_for_element_visible(locator, timeout or self.timeout)
        return element.text

    @allure.step("Check if element is displayed: {locator}")
    def is_displayed(self, locator, timeout=None):
        try:
            return self.wait_for_element_visible(locator, timeout).is_displayed()
        except Exception:
            return False

    @allure.step("Select dropdown option by visible text: {text}")
    def select_by_visible_text(self, locator, text, timeout=None):
        element = self.wait_for_element_clickable(locator, timeout or self.timeout)
        Select(element).select_by_visible_text(text)

    @allure.step("Select dropdown option by value: {value}")
    def select_by_value(self, locator, value, timeout=None):
        element = self.wait_for_element_clickable(locator, timeout or self.timeout)
        Select(element).select_by_value(value)

    # Advanced UI actions

    @allure.step("Hover over element: {locator}")
    def hover(self, locator, timeout=None):
        element = self.wait_for_element_visible(locator, timeout or self.timeout)
        self.actions.move_to_element(element).perform()

    @allure.step("Double-click element: {locator}")
    def double_click(self, locator, timeout=None):
        element = self.wait_for_element_clickable(locator, timeout or self.timeout)
        self.actions.double_click(element).perform()

    @allure.step("Right-click element: {locator}")
    def right_click(self, locator, timeout=None):
        element = self.wait_for_element_clickable(locator, timeout or self.timeout)
        self.actions.context_click(element).perform()

    # JavaScript and scrolling

    @allure.step("Scroll to element: {locator}")
    def scroll_to_element(self, locator, timeout=None):
        element = self.wait_for_element_present(locator, timeout or self.timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)

    @allure.step("Execute JavaScript: {script}")
    def execute_js(self, script, *args):
        try:
            return self.driver.execute_script(script, *args)
        except Exception as e:
            allure.attach(str(e), name="JS Execution Error", attachment_type=allure.attachment_type.TEXT)
            raise Exception(f"JavaScript execution failed: {str(e)}")
