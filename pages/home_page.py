# pages/home_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage, logger

class HomePage(BasePage):
    LOGGED_IN_INDICATOR = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')

    def is_logged_in(self):
        try:
            self.find_element(self.LOGGED_IN_INDICATOR)
            logger.info("Пользователь успешно залогинен.")
            return True
        except:
            logger.info("Пользователь не залогинен.")
            return False