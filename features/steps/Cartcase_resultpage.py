from selenium.webdriver.common.by import By
from behave import then

@then ('verify cart is empty')
def verify_results(context):
    expected_results = 'Your Amazon Cart is empty'
    actual_results = context.driver.find_element(By.CSS_SELECTOR, "div[class*='amazon-cart-is-empty']").text
    assert expected_results == actual_results, f'Error! Expected {expected_results} but {actual_results}'


