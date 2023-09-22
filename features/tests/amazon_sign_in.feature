# Created by ahdoy at 7/31/23
Feature: Test for sign in

  @smoke
  Scenario:  Verify that a user can click on orders
    Given Open Amazon page
    When Click on orders
    Then Verify Sign in text is Sign in

  Scenario:  Verify header has 5 links
    Given Open Amazon page
    When Click on best Sellers
    Then Verify Header has 5 links

  Scenario:  Verify UI elements on customer page
    Given Open Amazon page
    When Click on customer service
    Then Verify issue card has 11

  @smoke
  Scenario: Verify that a user can click on cart icon
    Given Open Amazon page
    When Click on shopping cart icon
    Then Verify cart result is Your Amazon Cart is empty


  Scenario: User can open and close Amazon Privacy Notice
   Given Open Amazon T&C page
   When Store original windows
   And Click on Amazon Privacy Notice
   And Switch to the newly opened window
   Then Verify Amazon Privacy Notice page is opened
   And User can close new window
   And Switch back to original


  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present


  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select Cell phones & Accessories
    And Search for iphone
    Then Verify Cell phones department selected