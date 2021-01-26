# Created by Joonil at 1/25/21
Feature: Test Scenarios for Logged out user clicking on Returns & Orders

  Scenario: Logged out user sees sign in page when clicking on Returns & Orders
    Given Open Amazon page
    When Click on Returns & Orders
    Then Sign in page is shown