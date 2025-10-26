# tests/test_registration.py

import unittest
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import config
from pages.signup_login_page import SignupLoginPage
from pages.account_info_page import AccountInfoPage
from pages.account_created_page import AccountCreatedPage
from selenium.webdriver.common.by import By
import time

# Настройка логгера (уже в base_page, но для тестов)
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format=config.LOG_FORMAT,
    filename=config.LOG_FILE,
    filemode='a'
)
logger = logging.getLogger(__name__)

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        logger.info("=== Инициализация теста ===")
        browser = config.BROWSER.lower()
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

        self.driver.maximize_window()
        self.driver.implicitly_wait(config.IMPLICIT_WAIT)
        logger.info(f"WebDriver инициализирован: {browser}")

        self.signup_login_page = SignupLoginPage(self.driver)
        self.signup_login_page.open(config.LOGIN_URL)
        self.signup_login_page.wait_for_page_load()

    def tearDown(self):
        self.driver.quit()
        logger.info("Браузер закрыт\n")

    def test_successful_registration(self):
        logger.info("=== Запуск теста успешной регистрации ===")
        user = config.VALID_USER

        self.signup_login_page.fill_signup_form(user['first_name'], user['email'])
        self.signup_login_page.submit_signup()

        account_info_page = AccountInfoPage(self.driver)
        account_info_page.wait_for_page_load()
        account_info_page.fill_account_info(
            user['first_name'], user['last_name'], user['password'],
            user['address'], user['city'], user['state'],
            user['zipcode'], user['country'], user['phone']
        )
        account_info_page.submit_create_account()

        account_created_page = AccountCreatedPage(self.driver)
        account_created_page.wait_for_page_load()
        success_message = account_created_page.get_success_message()
        self.assertIn("ACCOUNT CREATED!", success_message)
        logger.info(f"Регистрация успешна: {success_message}")

    def test_registration_with_invalid_data(self):
        logger.info("=== Запуск теста с некорректными данными ===")
        invalid_user = config.INVALID_USER

        self.signup_login_page.fill_signup_form(invalid_user['first_name'], invalid_user['email'])
        self.signup_login_page.submit_signup()

        form_opened = False
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="first_name"]')
            form_opened = True
        except NoSuchElementException:
            logger.info("Переход к полной регистрации не выполнен (ожидаемо).")

        self.assertFalse(form_opened, "Форма регистрации не должна открываться при некорректном email!")
        logger.info("Тест успешен — регистрация с некорректным email заблокирована.")