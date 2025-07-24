Feature: Get user from API

  @api @rest
  Scenario: Retrieve user by ID
    Given the API endpoint is "https://jsonplaceholder.typicode.com/users/1"
    When I send a GET request
    Then the response status code should be 200
    And the response should contain field "username"

  @postApi
  Scenario: Create a new post via POST request
    Given the API endpoint is "https://jsonplaceholder.typicode.com/posts"
    And the following JSON payload:
      | key    | value |
      | title  | foo   |
      | body   | bar   |
      | userId | 1     |
    When I send a POST request
    Then the response status code should be 201
    And the response JSON should match the schema "post_schema.json"