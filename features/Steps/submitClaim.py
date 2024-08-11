from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Constants for element IDs
URL = 'https://rpgroup.com/report-a-claim/details/accident-dk/'
COOKIE_BUTTON_ID = "wpnordic-cookie-care-consent-all-button"
SUBMIT_BUTTON_ID = "gform_submit_button_12"
FORM_HEADING_XPATH = "/html/body/div[3]/div/div/main/div/section/div/div/form/div[1]/div/div[1]/h3"
# Constants for form element IDs
NAME_FIELD_ID = "input_12_22"
PHONE_FIELD_ID = "input_12_12"

# Validation message IDs
VALIDATION_MESSAGES_EMPTY = [
    "validation_message_12_8", "validation_message_12_27", "validation_message_12_13",
    "validation_message_12_17", "validation_message_12_20", "validation_message_12_21",
    "validation_message_12_18", "validation_message_12_22", "validation_message_12_12"
]
VALIDATION_MESSAGES_SOME = [
    "validation_message_12_8", "validation_message_12_27", "validation_message_12_13",
    "validation_message_12_17", "validation_message_12_20", "validation_message_12_21",
    "validation_message_12_18"
]


@given(u'I am on the Claims Details Page/Form in Danish Language')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get(URL)
    context.browser.maximize_window()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, COOKIE_BUTTON_ID))
    ).click()


@when(u'User does not enter any details in the form')
def step_impl(context):
    pass


@when(u'User enters some details in the form')
def step_impl(context):
    navnEle = context.browser.find_element(By.ID, NAME_FIELD_ID)
    navnEle.send_keys("gdf")
    teleNumEle = context.browser.find_element(By.ID, PHONE_FIELD_ID)
    ac = ActionChains(context.browser)
    ac.scroll_to_element(teleNumEle).perform()
    teleNumEle.send_keys("6765")


@when(u'Clicks on the Submit button')
def step_impl(context):
    submit_button = context.browser.find_element(By.ID, SUBMIT_BUTTON_ID)
    ac = ActionChains(context.browser)
    ac.scroll_to_element(submit_button).perform()
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, SUBMIT_BUTTON_ID))
    ).click()


@then(u'Error messages should be displayed in red for all the empty fields')
def step_impl(context):
    for msg_id in VALIDATION_MESSAGES_EMPTY:
        WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.ID, msg_id))
        )


@then(u'Error messages should be displayed in red only for the empty fields')
def step_impl(context):
    for msg_id in VALIDATION_MESSAGES_SOME:
        WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.ID, msg_id))
        )


@then(u'The form should not be submitted, and the user should remain on the same details page')
def step_impl(context):
    heading = context.browser.find_element(By.XPATH, FORM_HEADING_XPATH)
    assert heading.text == "Ulykkesforsikring"
    print("Assertion passed: {}".format(heading.text))

    # Ensure browser is closed after the test
    context.browser.quit()
