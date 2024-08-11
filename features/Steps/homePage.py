from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
URL = 'https://rpgroup.com'
COOKIE_BUTTON_ID = "wpnordic-cookie-care-consent-all-button"
CLAIMS_TAB_XPATH = '//*[@id="menu-item-962"]/a'
EMERGENCY_CONTACTS_XPATH = "//h4[text()='Emergency Contacts']"
REPORT_A_CLAIM_XPATH = "//h4[text()='Report a Claim']"


@given("I am on the home page of 'rpgroup.com'")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get(URL)
    context.browser.maximize_window()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, COOKIE_BUTTON_ID))
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, CLAIMS_TAB_XPATH))
    )


@when('On the home page User hovers on the Claims tab')
def step_impl(context):
    claims_element = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, CLAIMS_TAB_XPATH))
    )
    ActionChains(context.browser).move_to_element(claims_element).perform()
    claims_element.click()


@then('Emergency Contacts section should be displayed')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, EMERGENCY_CONTACTS_XPATH))
    )
    assert context.browser.find_element(By.XPATH, EMERGENCY_CONTACTS_XPATH)


@then('Report a Claim section should be displayed')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, REPORT_A_CLAIM_XPATH))
    )
    assert context.browser.find_element(By.XPATH, REPORT_A_CLAIM_XPATH)


def after_scenario(context, scenario):
    context.browser.quit()
