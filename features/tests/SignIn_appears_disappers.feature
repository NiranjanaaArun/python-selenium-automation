# Created by rajan at 10/30/2022
Feature: Amazon feature file for Sign in button


  Scenario: Sign in btn appears and disappears
    Given Open Amazon.com page
    Then verify sign in is clickable
    When wait for 5 sec
    Then verify sign in is clickable
    Then verify Sign in disappears
