Feature: SignIn feature for logged out users

  Scenario: Verify that logged out users sees Sign in when clicking on Returns
    Given Open Amazon page
    When click orders
    Then Verify Sign In is opened