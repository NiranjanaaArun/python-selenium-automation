# Created by rajan at 10/30/2022
Feature: Test for 404 page


  Scenario: User is able to navigate to amazon blog
    Given amazon B08DYZCW3S5666896765 page
    And store original window
    When click dog image
    And switch to new window
    Then verify blog is opened
    And close blog
    And return to original window
