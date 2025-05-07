from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

from steps.reelly_off_page_steps import NEXT_BTN, PREV_PAGE_BTN


class OffPlanPage(Page):
    NEXT_BTN = (By.CSS_SELECTOR, "[wized='nextPageProperties']")
    PREV_PAGE_BTN = (By.CSS_SELECTOR, "[wized='previousPageProperties']")
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE = (By.CSS_SELECTOR, "[wized='loginButton']")
    NEW_OFF_PLAN_BTN = (By.CSS_SELECTOR, "[href='https://find.reelly.io/']")
    OFF_PLAN_BTN = (By.CSS_SELECTOR, "[wized='mobileTabProperties']")
    SECONDARY_BTN = (By.CSS_SELECTOR, "[href='https://soft.reelly.io/secondary-listings']")
    OFF_PLAN_TOP_BTN = (By.XPATH, "//a[text()='Off-plan']")

    def click_off_plan_option(self):
        self.wait_until_visible(*self.NEW_OFF_PLAN_BTN)
        self.click(*self.NEW_OFF_PLAN_BTN)
        self.wait_until_visible(*self.SECONDARY_BTN)
        self.click(*self.SECONDARY_BTN)
        self.wait_until_visible(*self.OFF_PLAN_BTN)
        self.click(*self.OFF_PLAN_BTN)

    def login_to_the_page(self):
        self.wait_until_visible(*self.EMAIL_FIELD)
        self.input_text('karpenkoalina1295@gmail.com', *self.EMAIL_FIELD)
        self.input_text('Pumunu20', *self.PASSWORD_FIELD)
        self.click(*self.CONTINUE)


    def click_next_button(self):
        clicks = 0
        max_clicks = 63

        while clicks < max_clicks:
            next_btn = self.driver.find_element(*NEXT_BTN)

            if next_btn.is_enabled():
                next_btn.click()
                clicks += 1
                print(f"Clicked 'Next' {clicks} time(s)")
                sleep(1)
            else:
                break

    def click_prev_button(self):
        clicks = 0
        max_clicks = 63

        while clicks < max_clicks:
            prev_page_btn = self.driver.find_element(*PREV_PAGE_BTN)

            if prev_page_btn.is_enabled():
                prev_page_btn.click()
                clicks += 1
                print(f"Clicked 'Previous' {clicks} time(s)")
                sleep(1)
            else:
                break