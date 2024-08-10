from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("I am on the home page of 'rpgroup.com'")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://rpgroup.com')
    context.browser.maximize_window()
    context.browser.find_element(By.ID, "wpnordic-cookie-care-consent-all-button").click()
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-item-962"]/a'))
    )


@when('On the home page User hovers on Claims tab')
def step_impl(context):
    claimelement = context.browser.find_element(By.XPATH, '//*[@id="menu-item-962"]/a')
    claimelement.click()
    #time.sleep(5)


@then('Emergency Contacts section should be displayed')
def step_impl(context):
    assert context.browser.find_element(By.XPATH, "//h4[text()='Emergency Contacts']")


@then('Report a Claim section should be displayed')
def step_impl(context):
    assert context.browser.find_element(By.XPATH, "//h4[text()='Report a Claim']")


