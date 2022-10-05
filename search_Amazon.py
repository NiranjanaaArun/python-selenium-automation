from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:/automation/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#search for "Dress"
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Dress')

# wait for 4 sec
sleep(4)

# click search
driver.find_element(By.ID, 'nav-search-submit-button').click()


# wait for 4 sec
sleep(4)

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
