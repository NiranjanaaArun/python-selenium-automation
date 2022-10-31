from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

dog_img= (By.CSS_SELECTOR,"#d")

@given("amazon {product} page")
def prod_page(context, product):
    context.driver.get("https://www.amazon.com/dp/B08DYZCW3S5666896765")

@given("store original window")
def store(context):
    context.original_window = context.driver.current_window_handle
    print('original_window', context.original_window)

@when("click dog image")
def click_dog(context):
    D = context.driver.find_element(*dog_img)
    D.click()

@when("switch to new window")
def switch(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_window= context.driver.window_handles
    print('current windows', current_window)
    context.driver.switch_to.window(current_window[1])

@then("verify blog is opened")
def blog_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/workplace'), message='doesnot contain the URL')
    print('current_window',context.driver.window_handles)

@then("close blog")
def blog_closed(context):
    context.driver.close()

@then("return to original window")
def return_original_window(context):
    context.driver.switch_to.window(context.original_window)


