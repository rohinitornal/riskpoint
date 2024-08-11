# Feature: demo
#   Scenario Outline: Verify that the user is able to navigate to different Language pages
#        Given I am on the Report a Claim page
#        When User clicks on the Accident Tab and selects <Language>
#        Then The correct page with heading <Heading> should be displayed
#        Examples:
#            | Language    | Heading               |
#            | Danish      | Ulykkesforsikring     |
#            | English     | Accident & Health     |
#            | Finnish     | Henkilövakuutukset    |
#            | Norwegian   | Ulykkesforsikring     |
#            | Swedish     | Olycksfallsförsäkring |
