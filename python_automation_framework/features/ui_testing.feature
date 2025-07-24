Feature: Login Feature


  Scenario: User logs in successfully
    Given I open the login page
    When I enter valid credentials
    Then I should be redirected to the dashboard


  @login @smoke
  Scenario: Successful login
    Given I am on the login page
    When I enter valid username "standard_user" and password "secret_sauce"
    And I click the login button
    Then I should see the dashboard