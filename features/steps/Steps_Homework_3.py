from selenium.webdriver.common.by import By
from behave import given, when

@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('click on orders and returns page')
def click_orders(context):
    orders = context.driver.find_element(By.XPATH, "//a[contains(@href, 'ref_=nav_orders_first')]//span[contains(@class, 'line-2')]")
    orders.click()


