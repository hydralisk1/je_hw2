from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ORDERS_BUTTON = (By.XPATH, "//a[@id='nav-orders']")
RESULTS_FOUND_MESSAGE = (By.XPATH, "//h1[@class='a-spacing-small']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Returns & Orders')
def click_orders(context):
    context.driver.find_element(*ORDERS_BUTTON).click()
    sleep(4)


@then('Sign in page is shown')
def verify_sign_in_page(context):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    expected_word = "Sign-In"
    assert expected_word == results_msg, "Expected word '{}' in message, but got '{}'".format(expected_word, results_msg)
