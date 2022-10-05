from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:/automation/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# click on cart
driver.find_element(By.CSS_SELECTOR, "a[href*='ref_=nav_cart']").click()

#Verify cart is empty
expected_results = 'Your Amazon Cart is empty'
actual_results = driver.find_element(By.CSS_SELECTOR, "div[class*='amazon-cart-is-empty']").text
assert expected_results==actual_results, f'Error! Expected {expected_results} but {actual_results}'

print('Test case passed')

driver.quit()