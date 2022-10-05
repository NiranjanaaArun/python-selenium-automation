# Created by rajan at 10/5/2022
Feature: Test scenarios for checking items in cart

  Scenario: User checks empty cart
    Given Open Amazon1 page
    When click on cart
    Then verify cart is empty
