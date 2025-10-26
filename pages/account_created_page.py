# pages/account_created_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage, logger

class AccountCreatedPage(BasePage):
    SUCCESS_TITLE = (By.CSS_SELECTOR, '.title.text-center')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a[data-qa="continue-button"]')

    def wait_for_page_load(self):
        try:
            self.find_element(self.CONTINUE_BUTTON)
            logger.info("Страница 'Account Created' загружена.")
        except:
            logger.exception("Страница 'Account Created' не загрузилась вовремя!")
            raise

    def get_success_message(self):
        return self.get_text(self.SUCCESS_TITLE)