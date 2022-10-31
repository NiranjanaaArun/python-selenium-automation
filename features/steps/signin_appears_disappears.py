from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

Sign_in = (By.CSS_SELECTOR, "#nav-signin-tooltip span[class= 'nav-action-inner']")

@then('verify sign in is clickable')
def verify_signIn_btn(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(Sign_in), message='Sign in is not clickable')

@when('wait for {time} sec')
def wait(context, time):
    sleep(int(5))

@then('verify Sign in disappears')
def signin_disappear(context):
    e = context.driver.wait.until(EC.invisibility_of_element(Sign_in), message='sign in did not disappear')

