from selenium.webdriver.common.by import By
from behave import then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SELECTED_DEPARTMENT= (By.CSS_SELECTOR, "#nav-subnav[data-category='{DEPARTMENT}']")

@then('Verify books {department} is selected')
def verify_books(context, department):
    context.driver.wait.until(EC.element_to_be_clickable(SELECTED_DEPARTMENT))

def get_department_locator(context, department):
    return[context.driver.SELECTED_DEPARTMENT[0], context.driver.SELECTED_DEPARTMENT[1].replace('{DEPARTMENT}', department)]

def verify_department(context, department):
    print('department => ', department)
    department_locator=context.get_department_locator(department)
    context.driver.wait.until(EC.presence_of_element_located(*department_locator))