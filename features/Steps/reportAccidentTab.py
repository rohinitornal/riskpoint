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
    print("love not yet")
    context.browser.find_element(By.ID, "wpnordic-cookie-care-consent-all-button").click()
    print("love clicked")
    # WebDriverWait(context, 10).until(
    #    EC.presence_of_element_located((By.XPATH, '//*[@id="menu-item-962"]/a'))
    # )
    print("love needs to wait")
    assert context
    claimelement = context.browser.find_element(By.XPATH, '//*[@id="menu-item-962"]/a')
    claimelement.click()
    print("love is claimed")
    startclaim = context.browser.find_element(By.XPATH,
                                              "//div[@data-id='menu-item-963']//a[text()='Start your claim here']")
    startclaim.click()
    print("love path found")
    time.sleep(3)
    print("I did love you....")


@when("Users click on Accident Tab and clicks on languages")
def step_impl(context):
    propertyelem = context.browser.find_element(By.XPATH, "//div[@class='accordion-header']/h3[text()='Property']")
    accele = context.browser.find_element(By.XPATH, "//div[@class='accordion-header']/h3[text()='Accident']")
    ac = ActionChains(context.browser)
    ac.scroll_to_element(propertyelem).perform()
    assert accele
    # context.browser.execute_script("arguments[0].scrollIntoView();", accele)
    accele.click()
    time.sleep(3)
    dk = context.browser.find_element(By.XPATH,
                                      '//*[@id="bbh-content"]/div/section[3]/div/div/div/div[2]/div/article[4]/div[2]/div/div/a[1]/div')
    assert dk

    print("Danish language exists...")
    dk.click()
    time.sleep(5)
    # en = context.browser.find_element(By.XPATH,
    #                                   "//*[@id='bbh-content']/div/section[3]/div/div/div/div[2]/div/article[4]/div[2]/div/div/a[2]")
    # assert en
    # print("English language exists...")
    # fi = context.browser.find_element(By.XPATH,
    #                                   "//*[@id='bbh-content']/div/section[3]/div/div/div/div[2]/div/article[4]/div[2]/div/div/a[3]")
    # assert fi
    # print("Finnish language exists...")
    # no = context.browser.find_element(By.XPATH,
    #                                   "//*[@id='bbh-content']/div/section[3]/div/div/div/div[2]/div/article[4]/div[2]/div/div/a[4]")
    # assert no
    # print("Norwegian language exists...")
    # se = context.browser.find_element(By.XPATH,
    #                                   "//*[@id='bbh-content']/div/section[3]/div/div/div/div[2]/div/article[4]/div[2]/div/div/a[5]")
    # assert se
    # print("Sweden language exists...")


@then("Then User should be able to see the heading")
def step_impl(context):
    heading = context.browser.find_element(By.XPATH, "//*[@id='field_12_31']/h3")
    assert heading.text == "Ulykkesforsikring"
    print("Assertion passed: {}".format(heading.text))
