from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
BASE_URL = 'https://rpgroup.com'
COOKIE_BUTTON_ID = "wpnordic-cookie-care-consent-all-button"
CLAIMS_TAB_XPATH = '//*[@id="menu-item-962"]/a'
START_CLAIM_XPATH = "//div[@data-id='menu-item-963']//a[text()='Start your claim here']"
PROPERTY_TAB_XPATH = "//div[@class='accordion-header']/h3[text()='Property']"
ACCIDENT_TAB_XPATH = "//div[@class='accordion-header']/h3[text()='Accident']"
HEADING_XPATH = "/html/body/div[3]/div/div/main/div/section/div/div/form/div[1]/div/div[1]/h3"
LANGUAGE_XPATH_TEMPLATE = "/html/body/div[3]/div/div/main/div/div/section[2]/div/div/div/div[2]/div/article[4]/div[2]/div/div/a[{}]"
LANGUAGES_LIST = ["Danish", "English", "Finnish", "Norwegian", "Swedish"]


@given("I am on the Report a Claim page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get(BASE_URL)
    context.browser.maximize_window()

    # Handle cookie consent
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, COOKIE_BUTTON_ID))
    ).click()

    # Navigate to the claim start page
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, CLAIMS_TAB_XPATH))
    ).click()

    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, START_CLAIM_XPATH))
    ).click()


@when("User clicks on the Accident Tab and selects {Language}")
def step_impl(context, Language):
    print(f"Selected Language: {Language}")

    # Scroll to the Property tab to ensure the Accident tab is in view
    property_elem = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, PROPERTY_TAB_XPATH))
    )
    ac = ActionChains(context.browser)
    ac.scroll_to_element(property_elem).perform()

    accident_elem = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, ACCIDENT_TAB_XPATH))
    )
    accident_elem.click()

    # Select the language-specific link
    lindex = LANGUAGES_LIST.index(Language) + 1
    language_xpath = LANGUAGE_XPATH_TEMPLATE.format(str(lindex))
    lang_elem = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, language_xpath))
    )
    lang_elem.click()


@then("The correct page with heading {Heading} should be displayed")
def step_impl(context, Heading):
    print(f"Expected Heading: {Heading}")

    heading_elem = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, HEADING_XPATH))
    )

    assert heading_elem.text == Heading, f"Expected heading '{Heading}', but got '{heading_elem.text}'"
    print("Assertion passed: {}".format(heading_elem.text))


def after_scenario(context, scenario):
    context.browser.quit()
