# Created by minhta at 2019-08-09
Feature: Subscribe with Paypal then sign up success
  # Enter feature description here

  Scenario: Subscribe with Paypal then sign up success
    Given I purchase package 1 personal at pricing tab by Paypal
    When  I signup successfully
    Then  I should see my balance changed
    And   I should see a chrome extension modal