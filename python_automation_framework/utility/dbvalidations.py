import allure

@allure.step("Asserting '{expected}' is in DB result")
def assert_text_in_result(result, expected):
    flat_result = [str(item[0]) for item in result if isinstance(item, tuple)]
    assert expected in flat_result, f"'{expected}' not found in result: {flat_result}"

@allure.step("Asserting DB result is greater than {value}")
def assert_result_greater_than(result, value):
    try:
        count = int(result[0][0])
        assert count > value, f"Expected result > {value}, got {count}"
    except Exception as e:
        raise AssertionError(f"Invalid DB result for numeric comparison: {e}")
