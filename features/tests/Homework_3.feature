# Created by rajan at 10/5/2022
Feature: Test for Amazon Search

  Scenario: Orders and returns page
      Given Open Amazon Page
      When click on orders and returns page
      Then verify sign in displayed
      Then verify email tab present
