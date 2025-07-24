
"""
DriverManager — Handles WebDriver initialization from config.ini

Supports: Chrome, Firefox, Edge
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config.config_manager import ConfigManager


class DriverManager:
    def __init__(self):
        self.driver = None
        self.config = ConfigManager()

    def get_driver(self):
        browser = self.config.get_browser().lower()
        headless = self.config.is_headless()
        window_size = self.config.get_window_size()

        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument(f"--window-size={window_size}")
            service = Service()
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
            # service = ChromeService(ChromeDriverManager().install())
            # self.driver = webdriver.Chrome(service=service, options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            width, height = window_size.split("x")
            options.add_argument(f"--width={width}")
            options.add_argument(f"--height={height}")
            service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service, options=options)

        elif browser == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument(f"--window-size={window_size}")
            service = EdgeService(EdgeChromiumDriverManager().install())
            self.driver = webdriver.Edge(service=service, options=options)

        else:
            raise ValueError(f"❌ Unsupported browser: {browser}")

        # Set implicit wait from config
        implicit_wait = self.config.get_implicit_wait()
        self.driver.implicitly_wait(implicit_wait)

        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
