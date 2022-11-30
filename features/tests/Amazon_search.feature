
Feature: Test scenario to check all products in page have price and and image

  Scenario: Verify all the products have price and image
    Given Open Amazon.com page
    When search coffee
    Then Verify all products have title and image


