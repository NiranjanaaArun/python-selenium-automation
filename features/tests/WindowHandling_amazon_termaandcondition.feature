# Created by rajan at 11/2/2022
Feature: Test for Window Handling


  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    And Store original windows
    When Click Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window
    And switch back to original window
