# Created by ahdoy at 7/30/23
Feature: Test for cart icon

  Scenario: Verify that a user can click on cart icon
    Given Open Amazon
    When Click on shopping cart icon
    Then Verify cart result is empty