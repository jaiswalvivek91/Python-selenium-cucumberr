import allure
import json
import jsonschema
from jsonschema import validate


@allure.step("Assert status code is {expected}")
def assert_status_code(response, expected):
    actual = response.status_code
    assert actual == expected, f"Expected status {expected}, but got {actual}"

@allure.step('Assert JSON response contains field: "{field}"')
def assert_json_field_exists(response, field):
    try:
        data = response.json()
    except Exception as e:
        raise AssertionError(f"Response is not valid JSON: {e}")
    assert field in data, f"Field '{field}' not found in response JSON"


@allure.step("Validate JSON response against schema")
def validate_json_schema(response, schema_filepath):
    try:
        data = response.json()
    except Exception as e:
        raise AssertionError(f"Response is not valid JSON: {e}")

    try:
        with open(schema_filepath, 'r') as f:
            schema = json.load(f)
    except FileNotFoundError:
        raise AssertionError(f"Schema file not found: {schema_filepath}")

    try:
        validate(instance=data, schema=schema)
    except jsonschema.ValidationError as e:
        raise AssertionError(f"JSON schema validation failed: {e.message}")
