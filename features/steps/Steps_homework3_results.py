from selenium.webdriver.common.by import By
from behave import then


@then('verify sign in displayed')
def verify_signin(context):
    expected_result = "Sign in"
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-box']//h1[contains(@class, 'spacing-small')]").text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'

@then('verify email tab present')
def verify_email_tab(context):
    assert context.driver.find_element(By.ID, "ap_email").is_displayed(), 'email field not shown'
