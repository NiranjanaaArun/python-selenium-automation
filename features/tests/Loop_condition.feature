# Created by rajan at 10/16/2022
Feature: Verify different colors in a product

  Scenario: Verify different colors in a product on Amazon page
    Given Open Amazon page
    When search for pink dress for woman
    And click on Harpa skater dress
    Then verify all the colors are clickable
