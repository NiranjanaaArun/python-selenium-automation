# Created by Svetlana at 4/4/19
Feature: Search for Dress

  Scenario: User can search for a product
    Given Open Google page
    When Input watch into search field
    And Click on search icon
    Then Product results for watch are shown


