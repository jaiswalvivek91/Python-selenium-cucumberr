# """
# Configuration manager for the automation framework
# """
# import configparser
# import os
# from dotenv import load_dotenv
#
# class ConfigManager:
#     def __init__(self, config_file="config/config.ini"):
#         load_dotenv()  # Load environment variables from .env file
#         self.config_file = config_file
#         self.config = configparser.ConfigParser()
#         self._load_config()
#
#     def _load_config(self):
#         """Load configuration from file"""
#         if os.path.exists(self.config_file):
#             self.config.read(self.config_file)
#         else:
#             raise FileNotFoundError(f"Configuration file {self.config_file} not found")
#
#     def get_config(self):
#         """Get the configuration object"""
#         return self.config
#
#     def get_base_url(self):
#         """Get base URL for the application"""
#         return self.config.get("DEFAULT", "base_url", fallback="https://example.com")
#
#     def get_browser(self):
#         """Get browser name"""
#         return self.config.get("DEFAULT", "browser", fallback="chrome")
#
#     def is_headless(self):
#         """Check if browser should run in headless mode"""
#         return self.config.getboolean("DEFAULT", "headless", fallback=True)
#
#     def get_db_config(self):
#         """Get database configuration"""
#         return {
#             "host": self.config.get("MYSQL", "host", fallback="localhost"),
#             "user": self.config.get("MYSQL", "user", fallback="root"),
#             "password": self.config.get("MYSQL", "password", fallback=""),
#             "database": self.config.get("MYSQL", "database", fallback="test_db")
#         }




"""
Configuration manager for the automation framework
"""
import configparser
import os
from dotenv import load_dotenv

class ConfigManager:
    def __init__(self, config_file="config/config.ini"):
        load_dotenv()
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self._load_config()

    def _load_config(self):
        if os.path.exists(self.config_file):
            self.config.read(self.config_file)
        else:
            raise FileNotFoundError(f"Configuration file {self.config_file} not found")

    def get_config(self):
        return self.config

    def get_base_url(self):
        return self.config.get("DEFAULT", "base_url", fallback="https://example.com")

    def get_browser(self):
        return self.config.get("DEFAULT", "browser", fallback="chrome")

    def is_headless(self):
        return self.config.getboolean("DEFAULT", "headless", fallback=True)

    def get_window_size(self):
        return self.config.get("DEFAULT", "window_size", fallback="1920x1080")

    def get_implicit_wait(self):
        return int(self.config.get("DEFAULT", "implicit_wait", fallback="10"))

    def get_db_config(self):
        return {
            "host": self.config.get("MYSQL", "host", fallback="localhost"),
            "user": self.config.get("MYSQL", "user", fallback="root"),
            "password": self.config.get("MYSQL", "password", fallback=""),
            "database": self.config.get("MYSQL", "database", fallback="test_db")
        }
