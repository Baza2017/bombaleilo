# tests/test_login.py

import unittest
import logging
from selenium import webdriver
import config
from pages.signup_login_page import SignupLoginPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
import time

# Настройка логгера
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format=config.LOG_FORMAT,
    filename=config.LOG_FILE,
    filemode='a'
)
logger = logging.getLogger(__name__)

class LoginTest(unittest.TestCase):
    def setUp(self):
        logger.info("=== Инициализация теста логина ===")
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

    def test_successful_login(self):
        logger.info("=== Запуск теста успешного логина ===")
        user = config.VALID_USER  # Предполагаем, что пользователь уже зарегистрирован

        self.signup_login_page.fill_login_form(user['email'], user['password'])
        self.signup_login_page.submit_login()

        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_logged_in(), "Логин не удался!")
        logger.info("Логин успешен.")