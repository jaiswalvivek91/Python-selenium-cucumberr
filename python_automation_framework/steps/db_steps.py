from behave import given, when, then
from database.db_client import DBClient
from utility.dbvalidations  import assert_text_in_result, assert_result_greater_than

@given("I connect to the database")
def step_impl(context):
    context.db = DBClient()

@when('I run the query "{query}"')
def step_impl(context, query):
    context.result = context.db.execute_query(query)

@then('the result should include "{expected}"')
def step_impl(context, expected):
    assert_text_in_result(context.result, expected)

@then("the result should be greater than 0")
def step_impl(context):
    assert_result_greater_than(context.result, 0)

def after_scenario(context, scenario):
    if hasattr(context, "db"):
        context.db.close()
