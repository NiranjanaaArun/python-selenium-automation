from selenium.webdriver.common.by import By
from behave import then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "ul[class*='g-top-micro swatches swatchesRectangle imageSwatches'] li")

@then('verify all the colors are clickable')
def verify_can_click_colors(context):

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    sleep(10)
    print(colors)


