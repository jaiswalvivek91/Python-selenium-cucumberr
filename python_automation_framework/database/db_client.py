import mysql.connector
from config.config_manager import ConfigManager
import allure

class DBClient:
    def __init__(self):
        self.config = ConfigManager()
        db_cfg = self.config.get_db_config()

        self.conn = mysql.connector.connect(
            host=db_cfg["host"],
            user=db_cfg["user"],
            password=db_cfg["password"],
            database=db_cfg["database"],
            port=db_cfg.get("port", 3306)
        )
        self.cursor = self.conn.cursor()

    @allure.step("Execute query: {query}")
    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
