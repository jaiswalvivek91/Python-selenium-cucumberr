Feature: Basic database validation

  @db @mysql
  Scenario: Verify user exists in the database
    Given I connect to the database
    When I run the query "SELECT username FROM users WHERE username = 'admin'"
    Then the result should include "admin"

  @db @mysql
  Scenario: Count the number of users in the system
    Given I connect to the database
    When I run the query "SELECT COUNT(*) FROM users"
    Then the result should be greater than 0
