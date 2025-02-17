from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

# init driver
s=Service('C:\Program Files\Automation\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
sleep(4)

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
# wait for 4 sec
sleep(4)
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')


driver.quit()
