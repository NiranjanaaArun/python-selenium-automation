from selenium.webdriver.common.by import By
from behave import then,given

Top_links=(By.CSS_SELECTOR, "div[class*='_p13n-zg-nav-tab-all_style_zg-tabs-li']")
Header = (By.ID, "zg_banner_text")

@then("Verify that all links open the correct URL")
def links(context):
    T_links = context.driver.find_elements(*Top_links)
    print(T_links)

    for i in range(len(T_links)):
        print (i)
        link_to_click= context.driver.find_elements(*Top_links)[i]
        link_text = link_to_click.text
        link_to_click.click()
        header_text = context.driver.find_element(*Header).text
        assert link_text in header_text, f'Expected  {link_text} to be in {header_text}'