# Created by minhta at 2019-08-09
Feature: As a new user without an account, I subscribe with Paypal and successfully sign up. I should see my balance to be unlimited and a sign up successfully modal.

  Scenario: Subscribe with Paypal, then sign up success
    Given I am at landing page
    And   I purchase package 0 personal at pricing tab by Paypal
    When  I signup successfully
    And   I confirm all policies
    Then  I should see a sign up successful modal
    And   I should see my balance to be 11
