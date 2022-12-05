# Created by rajan at 10/16/2022
Feature: Verify different colors in a product

  Scenario: Verify different colors in a product on Amazon page
    Given Opens Amazon product page B081YS2F7N
    Then verify all the colors are clickable
