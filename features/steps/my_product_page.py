from selenium.webdriver.common.by import By
from behave import then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "ul[class*='a-declarative a-button-toggle-group a-horizontal a-spacing-top-micro swatches swatchesRectangle imageSwatches'] li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
@then('verify all the colors are clickable')
def verify_can_click_colors(context):
    expected_colors = ['Army Green', 'Black', 'Blue', 'Burgundy', 'Caramel', 'Dark Blue', 'Denim Blue', 'Gray', 'Green', 'Khaki', 'Light-green', 'Orange', 'Pink', 'Purple', 'Red', 'Rose Red', 'Stripe Caramel', 'Stripe Gray', 'Stripe Green', 'Stripe Khaki','Stripe Red', 'Stripe Sapphire Blue', 'White', 'Yellow']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print('colors:', colors)
    for color in colors:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected color is expected_colors did not match {actual_colors}'

