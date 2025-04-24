from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC

EMAIL_FIELD = (By. ID, 'email-2')
PASSWORD_FIELD = (By.ID, 'field')
CONTINUE = (By. CSS_SELECTOR, "[wized='loginButton']")
OFF_PLAN_BTN = (By. CSS_SELECTOR, '.menu-old')
OFF_PLAN_TOP_BTN = (By. XPATH, "//a[text()='Off-plan']")
NEXT_BTN = (By.CSS_SELECTOR, "[wized='nextPageProperties']")
PREV_PAGE_BTN = (By.CSS_SELECTOR, "[wized='previousPageProperties']")

@given('Open Reelly main page')
def open_main_page(context):
    context.app.main_page.open_main_page()

@when('Log in to the page')
def login_to_the_page(context):
    context.app.base_page.wait_until_visible(*EMAIL_FIELD)
    context.app.base_page.input_text('karpenkoalina1295@gmail.com', *EMAIL_FIELD)
    context.app.base_page.input_text('Pumunu20', *PASSWORD_FIELD)
    context.app.base_page.click(*CONTINUE)

@when('Click on the off plan option at the left side menu')
def click_off_plan_option(context):
    context.app.base_page.wait_until_visible(*OFF_PLAN_BTN)
    context.app.base_page.click(*OFF_PLAN_BTN)

@then('Verify off plan page opens')
def verify_off_plan_opens(context):
    context.app.base_page.verify_text('Off-plan', *OFF_PLAN_TOP_BTN)

@then('Go to the final page')
def go_to_final_page(context):
    clicks = 0
    max_clicks = 63

    while clicks < max_clicks:
            next_btn = context.driver.find_element(*NEXT_BTN)

            if next_btn.is_enabled():
                next_btn.click()
                clicks += 1
                print(f"Clicked 'Next' {clicks} time(s)")
                sleep(1)
            else:
                break

@then('Go back to the first page')
def go_back_to_first_page(context):
    clicks = 0
    max_clicks = 63

    while clicks < max_clicks:
        prev_page_btn = context.driver.find_element(*PREV_PAGE_BTN)

        if prev_page_btn.is_enabled():
            prev_page_btn.click()
            clicks += 1
            print(f"Clicked 'Next' {clicks} time(s)")
            sleep(1)
        else:
            break
