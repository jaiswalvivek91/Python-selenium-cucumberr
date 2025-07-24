import os
from allure_commons.types import AttachmentType
import allure
from datetime import datetime

def attach_screenshot(driver, step_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_folder = "reports/screenshots"
    os.makedirs(screenshot_folder, exist_ok=True)
    filename = f"{step_name}_{timestamp}.png".replace(" ", "_")
    filepath = os.path.join(screenshot_folder, filename)
    driver.save_screenshot(filepath)
    allure.attach.file(filepath, name=step_name, attachment_type=AttachmentType.PNG)
