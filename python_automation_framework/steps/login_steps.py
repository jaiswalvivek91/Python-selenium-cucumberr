from behave import given, when, then
from pages.login_page import LoginPage
from behave import given, when, then
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import allure



@given('I open the login page')
def open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

@when('I enter valid credentials')
def enter_credentials(context):
    context.login_page.login('test_user', 'test_pass')

@then('I should be redirected to the dashboard')
def verify_dashboard(context):
    assert context.login_page.is_dashboard_displayed(), "Dashboard not displayed"



"""
Step definitions for login functionality
"""


@given('I am on the login page')
def step_navigate_to_login(context):
    with allure.step("Navigate to login page"):
        context.login_page = LoginPage(context.driver)
        context.login_page.navigate_to_login()

@when('I enter valid username "{username}" and password "{password}"')
def step_enter_valid_credentials(context, username, password):
    with allure.step(f"Enter username: {username} and password: {password}"):
        context.login_page.enter_username(username)
        context.login_page.enter_password(password)

@when('I enter invalid username "{username}" and password "{password}"')
def step_enter_invalid_credentials(context, username, password):
    with allure.step(f"Enter invalid username: {username} and password: {password}"):
        context.login_page.enter_username(username)
        context.login_page.enter_password(password)

@when('I click the login button')
def step_click_login_button(context):
    with allure.step("Click login button"):
        context.login_page.click_login()

@then('I should see the dashboard')
def step_verify_redirect_to_dashboard(context):
    # with allure.step("Verify redirect to dashboard"):
        context.dashboard_page = DashboardPage(context.driver)
        assert context.dashboard_page.is_dashboard_loaded(), "Dashboard was not loaded"

@then('I should see the welcome message')
def step_verify_welcome_message(context):
    with allure.step("Verify welcome message is displayed"):
        context.dashboard_page = DashboardPage(context.driver)
        assert context.dashboard_page.is_welcome_message_displayed(), "Welcome message not displayed"

@then('I should see an error message')
def step_verify_error_message(context):
    with allure.step("Verify error message is displayed"):
        assert context.login_page.is_error_message_displayed(), "Error message not displayed"

@then('I should remain on the login page')
def step_verify_remain_on_login_page(context):
    with allure.step("Verify still on login page"):
        assert context.login_page.is_login_page_loaded(), "Not on login page"