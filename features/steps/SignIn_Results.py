from selenium.webdriver.common.by import By
from behave import then

@then('Verify Sign In is opened')
def verify_sign_in_opened(context):
    context.app.sign_in_page.verify_signin_opened
