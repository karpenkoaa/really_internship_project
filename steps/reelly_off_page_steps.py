from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC

EMAIL_FIELD = (By. ID, 'email-2')
PASSWORD_FIELD = (By.ID, 'field')
CONTINUE = (By. CSS_SELECTOR, "[wized='loginButton']")
NEW_OFF_PLAN_BTN = (By. CSS_SELECTOR, "[href='https://find.reelly.io/']")
OFF_PLAN_BTN = (By. CSS_SELECTOR, "[wized='mobileTabProperties']")
SECONDARY_BTN = (By. CSS_SELECTOR, "[href='https://soft.reelly.io/secondary-listings']")
OFF_PLAN_TOP_BTN = (By. XPATH, "//a[text()='Off-plan']")
NEXT_BTN = (By.CSS_SELECTOR, "[wized='nextPageProperties']")
PREV_PAGE_BTN = (By.CSS_SELECTOR, "[wized='previousPageProperties']")

@given('Open Reelly main page')
def open_main_page(context):
    context.app.main_page.open_main_page()

@when('Log in to the page')
def login_to_the_page(context):
    context.app.off_plan_page.login_to_the_page()

@when('Click on the off plan option at the left side menu')
def click_off_plan_option(context):
    context.app.off_plan_page.click_off_plan_option()

@then('Verify off plan page opens')
def verify_off_plan_opens(context):
    context.app.base_page.verify_text('Off-plan', *OFF_PLAN_TOP_BTN)

@then('Go to the final page')
def go_to_final_page(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    context.app.off_plan_page.click_next_button()

@then('Go back to the first page')
def go_back_to_first_page(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    context.app.off_plan_page.click_prev_button()
