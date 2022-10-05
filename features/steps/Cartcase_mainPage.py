from selenium.webdriver.common.by import By
from behave import given, when

@given('Open Amazon1 page')
def open_amazon1(context):
    context.driver.get('https://www.amazon.com/')

@when('click on cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='ref_=nav_cart']").click()


