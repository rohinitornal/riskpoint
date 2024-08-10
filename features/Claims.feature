Feature: Claims

    Scenario: Verify the Home Page of RiskPoint Group
        Given I am on the home page of 'rpgroup.com'
        When On the home page User hovers on Claims tab
        Then Emergency Contacts section should be displayed
        And Report a Claim section should be displayed

    Scenario: Verify that the user is navigated to Report a Claim Page
        Given I am on the Report a claim section on home page
        When User clicks on the claims tab
        And User clicks on the link 'Start your claim here' on Report a Claim section
        Then User should be directed to Report a Claim Page

    Scenario Outline: Verify that the user is able to navigate to different Language pages
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

    Scenario: Verify that user enters no details in the form
        Given I am on Claims Details Page/Form in Danish Language
        When User does not enter any details in the form
        And Clicks on Submit button
        Then Error messages should be displayed in Red color for all the empty fields
        And Form should not be submitted and user should be on the same details page


    Scenario: Verify that user enters few details in the form and submits
        Given I am on Claims Details Page/Form in Danish Language
        When User enters few details in the form
        And Clicks on Submit button
        Then Error messages should be displayed in Red color only for empty fields
        And Form should not be submitted and user should be on the same details page
