from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

from steps.reelly_off_page_steps import NEXT_BTN, PREV_PAGE_BTN


class OffPlanPage(Page):
    NEXT_BTN = (By.CSS_SELECTOR, "[wized='nextPageProperties']")
    PREV_PAGE_BTN = (By.CSS_SELECTOR, "[wized='previousPageProperties']")

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