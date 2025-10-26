# pages/account_info_page.py

from selenium.webdriver.common.by import By
import time
from .base_page import BasePage, logger

class AccountInfoPage(BasePage):
    TITLE_MR_RADIO = (By.CSS_SELECTOR, '[data-qa="title"] input[value="Mr"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[data-qa="first_name"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[data-qa="last_name"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[data-qa="password"]')
    ADDRESS_INPUT = (By.CSS_SELECTOR, 'input[data-qa="address"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[data-qa="city"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[data-qa="state"]')
    ZIPCODE_INPUT = (By.CSS_SELECTOR, 'input[data-qa="zipcode"]')
    COUNTRY_SELECT = (By.CSS_SELECTOR, 'select[data-qa="country"]')
    PHONE_INPUT = (By.CSS_SELECTOR, 'input[data-qa="mobile_number"]')
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="create-account"]')

    def wait_for_page_load(self):
        try:
            self.find_element(self.FIRST_NAME_INPUT)
            logger.info("Форма полной регистрации загружена.")
        except:
            logger.exception("Форма полной регистрации не загрузилась вовремя!")
            raise

    def fill_account_info(self, first_name, last_name, password, address, city, state, zipcode, country, phone):
        self.click(self.TITLE_MR_RADIO)
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.send_keys(self.ADDRESS_INPUT, address)
        self.send_keys(self.CITY_INPUT, city)
        self.send_keys(self.STATE_INPUT, state)
        self.send_keys(self.ZIPCODE_INPUT, zipcode)
        self.select_country(country)
        self.send_keys(self.PHONE_INPUT, phone)
        logger.info(f"Заполнены данные аккаунта, выбрана страна: {country}, телефон: {phone}")

    def select_country(self, country):
        country_dropdown = self.find_element(self.COUNTRY_SELECT)
        for option in country_dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.text.strip() == country:
                option.click()
                break

    def submit_create_account(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)
        logger.info("Нажата кнопка 'Create Account'")
        time.sleep(10)  # Для ожидания перехода