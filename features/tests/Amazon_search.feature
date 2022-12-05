
Feature: Test scenario to check all products in page have price and and image

  Scenario: Verify all the products have price and image
    Given Open Amazon.com page
    When search coffee
    #Then Verify all products have title and image


  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option is present

  Scenario: User can select and search a department
    Given Open Amazon page
    When Select department by value stripbooks
    And search for Faust
    Then Verify books department is selected
