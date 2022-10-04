from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:/automation/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# click on orders and returns
orders = driver.find_element(By.XPATH, "//a[contains(@href, 'ref_=nav_orders_first')]//span[contains(@class, 'line-2')]")
orders.click()

# verify sign in button
expected_result = "Sign in"
actual_result = driver.find_element(By.XPATH, "//div[@class='a-box']//h1[contains(@class, 'spacing-small')]").text
assert expected_result==actual_result, f'Error! Expected {expected_result}, but got {actual_result}'

print("Test case passed")

# verify email field present
assert driver.find_element(By.ID, "ap_email").is_displayed(), 'email field not shown'

print("Test case passed")



driver.quit()