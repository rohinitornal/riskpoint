from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given("I am on the Report a claim section on home page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://rpgroup.com')
    context.browser.maximize_window()
    context.browser.find_element(By.ID, "wpnordic-cookie-care-consent-all-button").click()
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-item-962"]/a'))
    )


@when("User clicks on the claims tab")
def step_impl(context):
    claimelement = context.browser.find_element(By.XPATH, '//*[@id="menu-item-962"]/a')
    claimelement.click()


@when("User clicks on the link 'Start your claim here' on Report a Claim section")
def step_impl(context):
    startclaim = context.browser.find_element(By.XPATH,
                                              "//div[@data-id='menu-item-963']//a[text()='Start your claim here']")
    startclaim.click()
    time.sleep(3)


@then("User should be directed to Report a Claim Page")
def step_impl(context):
    h1_element = context.browser.find_element(By.XPATH, "//h1[text()='Report a Claim']")
    assert h1_element.text == "Report a Claim", "The H1 text does not match 'Report a Claim'"
    print("Assertion passed: The H1 text is 'Report a Claim'")
