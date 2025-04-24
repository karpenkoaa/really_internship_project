# Created by alinakarpenko at 4/23/25
Feature: Off plan page test

  Scenario: User can open the off plan page and go through the pagination
    Given Open Reelly main page
    When Log in to the page
    And Click on the off plan option at the left side menu
    Then Verify off plan page opens
    And Go to the final page
    And Go back to the first page