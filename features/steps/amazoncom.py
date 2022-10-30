from selenium.webdriver.common.by import By
from behave import given, when

search_tab = (By.ID, "twotabsearchtextbox")
search_btn = (By.ID, "nav-search-submit-button")

@given('Open Amazon.com page')
def main_page(context):
    context.driver.get('https://www.amazon.com')

@when('search {product_name}')
def mug(context, product_name):
    tab = context.driver.find_element(*search_tab)
    tab.send_keys(product_name)
    context.driver.find_element(*search_btn).click()

CURRENT_COLOR = (By.CSS_SELECTOR, "div#variation_color_name span[class='selection']")
