from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
BASE_URL = 'https://rpgroup.com'
COOKIE_BUTTON_ID = "wpnordic-cookie-care-consent-all-button"
CLAIMS_TAB_XPATH = '//*[@id="menu-item-962"]/a'
START_CLAIM_XPATH = "//div[@data-id='menu-item-963']//a[text()='Start your claim here']"
REPORT_CLAIM_HEADING_XPATH = "//h1[text()='Report a Claim']"


@given("I am on the Report a Claim section on the home page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get(BASE_URL)
    context.browser.maximize_window()

    # Handle cookie consent
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, COOKIE_BUTTON_ID))
    ).click()

    # Wait until the Claims tab is present
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, CLAIMS_TAB_XPATH))
    )


@when("User clicks on the claims tab")
def step_impl(context):
    claims_tab = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, CLAIMS_TAB_XPATH))
    )
    claims_tab.click()


@when("User clicks on the link 'Start your claim here' in the Report a Claim section")
def step_impl(context):
     WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, START_CLAIM_XPATH))
    ).click()


@then("User should be directed to the Report a Claim Page")
def step_impl(context):
    report_claim_heading = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, REPORT_CLAIM_HEADING_XPATH))
    )
    import time
    time.sleep(3)
    assert report_claim_heading.text == "Report a Claim", "The H1 text does not match 'Report a Claim'"
    print("Assertion passed: The H1 text is 'Report a Claim'")


def after_scenario(context, scenario):
    context.browser.quit()
