Feature: Claims
    Scenario:
        Given I am on the home page of 'rpgroup.com'
        When On the home page User hovers on Claims tab
        Then Emergency Contacts section should be displayed
        And Report a Claim section should be displayed

    Scenario:
        Given I am on the Report a claim section on home page
        When User clicks on the claims tab
        And User clicks on the link 'Start your claim here' on Report a Claim section
        Then User should be directed to Report a Claim Page

    Scenario Outline:
        Given I am on Report a Claim page
        When Users click on Accident Tab and clicks on <Language>
        Then User should be able to see the <Heading>
        Examples:
            | Language | Heading  |
            | Danish   | Ulykkesforsikring  |
            | English  | Accident & Health  |
            | Finnish  | Henkilövakuutukset  |
            | Norwegian| Ulykkesforsikring  |
            | Swedish  | Olycksfallsförsäkring  |

