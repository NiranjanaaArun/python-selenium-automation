from selenium.webdriver.common.by import By
from behave import when,then
from time import sleep

search_results = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
product_title = (By.CSS_SELECTOR, "h2 span.a-text-normal")
product_img = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")

@then('Verify all products have title and image')
def coffee_results(context):
    all_products = context.driver.find_elements(*search_results)
    print(all_products)
    sleep(2)

    for product in all_products:
        title=product.find_element(*product_title).text
        print(title)
        assert title, 'Error! Title should not be blank'
        img=product.find_element(*product_img)
        assert img, 'is not displayed'