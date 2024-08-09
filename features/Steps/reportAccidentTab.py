from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given("I am on Report a Claim page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://rpgroup.com')
    context.browser.maximize_window()
    context.browser.find_element(By.ID, "wpnordic-cookie-care-consent-all-button").click()

    claimelement = context.browser.find_element(By.XPATH, '//*[@id="menu-item-962"]/a')
    claimelement.click()
    startclaim = context.browser.find_element(By.XPATH,
                                              "//div[@data-id='menu-item-963']//a[text()='Start your claim here']")
    startclaim.click()


@when("Users click on Accident Tab and clicks on {Language}")
def step_impl(context, Language):
    print(Language)
    propertyelem = context.browser.find_element(By.XPATH, "//div[@class='accordion-header']/h3[text()='Property']")
    accele = context.browser.find_element(By.XPATH, "//div[@class='accordion-header']/h3[text()='Accident']")
    assert accele

    accele.click()
    time.sleep(3)

    ac = ActionChains(context.browser)
    ac.scroll_to_element(propertyelem).perform()

    lang_list = ["Danish", "English", "Finnish", "Norwegian", "Swedish"]
    lindex = lang_list.index(Language) + 1
    xpath = "/html/body/div[3]/div/div/main/div/div/section[2]/div/div/div/div[2]/div/article[4]/div[2]/div/div/a[{}]"\
        .format(str(lindex))
    acc_health = context.browser.find_element(By.XPATH, xpath)
    print("Danish language exists...")
    assert acc_health
    acc_health.click()


@then("User should be able to see the {Heading}")
def step_impl(context, Heading):
    print(Heading)
    xpath = "/html/body/div[3]/div/div/main/div/section/div/div/form/div[1]/div/div[1]/h3"
    heading = context.browser.find_element(By.XPATH, xpath)

    assert heading.text == Heading
    print("Assertion passed: {}".format(heading.text))
