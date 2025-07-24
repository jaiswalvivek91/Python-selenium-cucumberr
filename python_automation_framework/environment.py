import os
from driver_manager import DriverManager
from utility.helpers import attach_screenshot

def before_all(context):
    context.driver_manager = DriverManager()
    context.driver = context.driver_manager.get_driver()

def after_step(context, step):
    if step.status == "failed":
        attach_screenshot(context.driver, step.name)

def after_all(context):
    context.driver_manager.quit_driver()
