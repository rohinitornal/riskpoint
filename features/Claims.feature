Feature: Claims

    Scenario: Verify the Home Page of RiskPoint Group
        Given I am on the home page of 'rpgroup.com'
        When On the home page User hovers on the Claims tab
        Then Emergency Contacts section should be displayed
        And Report a Claim section should be displayed

    Scenario: Verify that the user is navigated to Report a Claim Page
        Given I am on the Report a Claim section on the home page
        When User clicks on the Claims tab
        And User clicks on the link 'Start your claim here' in the Report a Claim section
        Then User should be directed to the Report a Claim Page

    Scenario Outline: Verify that the user is able to navigate to different Language pages
        Given I am on the Report a Claim page
        When User clicks on the Accident Tab and selects <Language>
        Then The correct page with heading <Heading> should be displayed
        Examples:
            | Language    | Heading               |
            | Danish      | Ulykkesforsikring     |
            | English     | Accident & Health     |
            | Finnish     | Henkilövakuutukset    |
            | Norwegian   | Ulykkesforsikring     |
            | Swedish     | Olycksfallsförsäkring |

    Scenario: Verify that the form displays error messages when no details are entered
        Given I am on the Claims Details Page/Form in Danish Language
        When User does not enter any details in the form
        And Clicks on the Submit button
        Then Error messages should be displayed in red for all the empty fields
        And The form should not be submitted, and the user should remain on the same details page

    Scenario: Verify that the form displays error messages only for empty fields when some details are entered
        Given I am on the Claims Details Page/Form in Danish Language
        When User enters some details in the form
        And Clicks on the Submit button
        Then Error messages should be displayed in red only for the empty fields
        And The form should not be submitted, and the user should remain on the same details page
