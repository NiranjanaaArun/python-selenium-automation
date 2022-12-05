from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

search_tab = (By.ID, "twotabsearchtextbox")
search_btn = (By.ID, "nav-search-submit-button")
language_hover = (By.CSS_SELECTOR, ".icp-nav-flag-us")
spanish_text= (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
DEPARTMENT_SELECTION = (By.ID,'searchDropdownBox')
@given('Open Amazon page')
def main_page(context):
    context.driver.get('https://www.amazon.com')
    #context.app.main_page.open_main()

@given('Opens Amazon product page {product}')
def main_p(context, product):
    context.driver.get('https://www.amazon.com/dp/B08JHKQPBV')


@when('search for {product_name}')
def mug(context, product_name):
    tab = context.driver.find_element(*search_tab)
    tab.send_keys(product_name)
    context.driver.find_element(*search_btn).click()
    #context.app.main_page.search_product(product)

@when('click orders')
def order(context):
    context.app.main_page.click_orders()

@when ('Hover over language options')
def hover_on_language(context):
    language_selection = context.driver.find_element(*language_hover)
    Actions = ActionChains(context.driver)
    Actions.move_to_element(language_selection)
    Actions.perform()
    time.sleep(4)

@when ('Select department by value {value}')
def selectdropdown(context, value):
    select= Select(context.driver.find_element(*DEPARTMENT_SELECTION))
    select.select_by_value(f'search-alias={value}-intl-ship')
@then('Verify Spanish option is present')
def spanish_option(context):
    expected_result="español - ES"
    actual_result=context.driver.find_element(*spanish_text).text
    assert expected_result == actual_result, f'expected {expected_result} got actual {actual_result}'



