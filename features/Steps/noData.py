from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given(u'I am on Claims Details Page/Form in Danish Language')
def step_impl(context):

    context.browser = webdriver.Chrome()
    context.browser.get('https://rpgroup.com/report-a-claim/details/accident-dk/')
    #context.browser.maximize_window()
    context.browser.find_element(By.ID, "wpnordic-cookie-care-consent-all-button").click()


@when(u'User does not enter any details in the form')
def step_impl(context):
    pass


@when(u'Clicks on Submit button')
def step_impl(context):
    submit = context.browser.find_element(By.ID, "gform_submit_button_12")
    ac = ActionChains(context.browser)
    ac.scroll_to_element(submit).perform()
    assert submit
    submit.click()


@then(u'Error messages should be displayed in Red color for all the empty fields')
def step_impl(context):
    v_msgs = ["validation_message_12_22",
              "validation_message_12_8",
              "validation_message_12_27",
              "validation_message_12_12",
              "validation_message_12_13",
              "validation_message_12_17",
              "validation_message_12_20",
              "validation_message_12_21",
              "validation_message_12_17",
              "validation_message_12_18"]

    for msg in v_msgs:
        WebDriverWait(context.browser, 3).until(
            EC.presence_of_element_located((By.ID, msg))
        )


@then(u'Form should not be submitted and user should be on the same details page')
def step_impl(context):
    xpath = "/html/body/div[3]/div/div/main/div/section/div/div/form/div[1]/div/div[1]/h3"
    heading = context.browser.find_element(By.XPATH, xpath)

    assert heading.text == "Ulykkesforsikring"
    print("Assertion passed: {}".format(heading.text))
