from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

Privacy_Notice= (By.CSS_SELECTOR,"a[href='https://www.amazon.com/privacy']")

@given ("Open Amazon {desired_page}")
def page (context, desired_page):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")

@given("Store original windows")
def original_window(context):
        context.original_window = context.driver.current_window_handle
        print('original_window', context.original_window)

@when("Click Amazon Privacy Notice link")
def privacy_notice(context):
    PN= context.driver.find_element(*Privacy_Notice).click()

@when("Switch to the newly opened window")
def switch(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_window= context.driver.window_handles
    print('current windows', current_window)
    context.driver.switch_to.window(current_window[1])

@then("Verify Amazon Privacy Notice page is opened")
def Privacy_Notice_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer'), message='doesnot contain the URL')
    print('current_window',context.driver.window_handles)

@then("User can close new window")
def new_window_closed(context):
    context.driver.close()

@then("switch back to original window")
def return_original_window(context):
    context.driver.switch_to.window(context.original_window)

