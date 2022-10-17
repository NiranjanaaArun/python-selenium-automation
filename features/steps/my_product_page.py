from selenium.webdriver.common.by import By
from behave import then

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR= (By.CSS_SELECTOR, "#variation_color_name .selection")

@then('verify all the colors are clickable')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Green', 'Pink', 'Royal Blue']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

for color in colors:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]

    assert expected_colors == actual_colors, \
        f'Expected colors {expected_colors} did not match actual {actual_colors}'
