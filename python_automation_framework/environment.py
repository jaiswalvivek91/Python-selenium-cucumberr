import os
from driver_manager import DriverManager
from utility.helpers import attach_screenshot

def before_scenario(context, scenario):
    """
    Runs before each scenario.
    Creates a new browser instance for each scenario.
    """
    context.driver_manager = DriverManager()
    context.driver = context.driver_manager.get_driver()

def after_step(context, step):
    """
    Runs after each step.
    Takes screenshot if step failed.
    """
    if step.status == "failed":
        attach_screenshot(context.driver, step.name)

def after_scenario(context, scenario):
    """
    Runs after each scenario.
    Quits the browser instance to ensure fresh browser for next scenario.
    """
    if hasattr(context, "driver_manager"):
        context.driver_manager.quit_driver()
        context.driver = None
        context.driver_manager = None

# (Optional) Use before_all and after_all for global setup/teardown if needed

def before_all(context):
    """
    Global setup before all tests (do not create browser here).
    """
    pass

def after_all(context):
    """
    Global teardown after all tests (do not quit browser here).
    """
    pass
