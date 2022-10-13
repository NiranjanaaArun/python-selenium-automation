from selenium.webdriver.common.by import By
from behave import given, then

No_of_links = By.CSS_SELECTOR("div[class*='_p13n-zg-nav-tab-all_style_zg-tabs-li-']")

@given('Open Bestseller page')
def Bestseller_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('verify there are {expected_link_count} links')
def verify_links(context, expected_link_count):
    expected_link_count= int(expected_link_count)
    links = context.driver.find_elements(*No_of_links)
    assert len(links) == expected_link_count, f'Expected{expected_link_count} but got otherwise'



