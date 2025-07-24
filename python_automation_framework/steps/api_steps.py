from behave import given, when, then
from api.api_client import APIClient
from utility.apivalidations import assert_status_code, assert_json_field_exists, validate_json_schema


@given('the API endpoint is "{url}"')
def step_impl(context, url):
    context.api_url = url

@when("I send a GET request")
def step_impl(context):
    context.response = APIClient.get(context.api_url)

@then("the response status code should be {status_code:d}")
def step_impl(context, status_code):
    assert_status_code(context.response, status_code)

@then('the response should contain field "{field}"')
def step_impl(context, field):
    assert_json_field_exists(context.response, field)


@given('the following JSON payload')
def step_impl(context):
    context.payload = {}
    for row in context.table:
        key, value = row['key'], row['value']
        if key == "userId":
            value = int(value)      # Convert to integer for schema compliance
        context.payload[key] = value


@when("I send a POST request")
def step_impl(context):
    context.response = APIClient.post(context.api_url, json=context.payload)

@then('the response JSON should match the schema "{schema_file}"')
def step_impl(context, schema_file):
    # Load schema file from schemas folder
    schema_path = f"schemas/{schema_file}"
    validate_json_schema(context.response, schema_path)