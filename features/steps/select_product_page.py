from selenium.webdriver.common.by import By
from behave import when

product_ID= (By.CSS_SELECTOR, "a[href*='/Harpa-Womens-Skater-Dress-GR2766_Pink_Large/dp/B015ORI2GC']")

@when("click on {my_product}")
def dress(context, my_product):
    context.driver.find_element(*product_ID).click()