from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:/automation/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fyour-account%2F%3F_encoding%3DUTF8%26ref_%3Dnav_em_hd_re_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&ref_%3Dnav_em_hd_clc_signin_0_1_1_32')

#Logo
#driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo' and @role='img']").click()

#email Field
#driver.find_element(By.ID, "ap_email")

#continue
#driver.find_element(By.ID, 'continue').click()

#need help link
#driver.find_element(By.XPATH, '//div[@class="a-section"]//span[@class="a-expander-prompt"]').click()

#forgot your password link
#driver.find_element(By.XPATH, '//a[@class="a-link-normal"]').click()
#driver.find_element(By.XPATH, '//body[contains(@class, "ap-locale-en_IN a-m-us a-aui_72554-c ")]')

#other issues with sign in link button
#driver.find_element(By.ID, 'ap-other-signin-issues-link').click()
#driver.get('https://www.amazon.in/gp/help/customer/account-issues/ref=ap_login_with_otp_claim_collection?ie=UTF8')
#sleep(4)

#create your Amazon account button
#driver.find_element(By.ID, 'createAccountSubmit')

#conditions of use link
#driver.find_element(By.XPATH, "//a[@class='a-link-normal' and contains(@href, 'cou?ie=UTF8&nodeId=200545940')]").click()

#Privacy notice link
driver.find_element(By.XPATH, "//a[@class='a-link-normal' and contains(@href, 'privacy_notice?ie=UTF8&nodeId')]").click()

driver.quit()


