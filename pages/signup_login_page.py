# pages/signup_login_page.py

from selenium.webdriver.common.by import By
import time
from .base_page import BasePage, logger

class SignupLoginPage(BasePage):
    SIGNUP_NAME_INPUT = (By.CSS_SELECTOR, 'input[data-qa="signup-name"]')
    SIGNUP_EMAIL_INPUT = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    SIGNUP_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="signup-button"]')
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, 'input[data-qa="login-email"]')
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[data-qa="login-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="login-button"]')
    SIGNUP_FORM = (By.CSS_SELECTOR, '.signup-form')

    def wait_for_page_load(self):
        try:
            self.find_element(self.SIGNUP_FORM)
            logger.info("Форма Signup/Login успешно загружена.")
        except:
            logger.exception("Форма Signup/Login не загрузилась вовремя!")
            raise

    def fill_signup_form(self, name, email):
        self.send_keys(self.SIGNUP_NAME_INPUT, name)
        self.send_keys(self.SIGNUP_EMAIL_INPUT, email)
        logger.info(f"Введены данные: Name={name}, Email={email}")

    def submit_signup(self):
        self.click(self.SIGNUP_BUTTON)
        logger.info("Нажата кнопка 'Signup'")

    def fill_login_form(self, email, password):
        self.send_keys(self.LOGIN_EMAIL_INPUT, email)
        self.send_keys(self.LOGIN_PASSWORD_INPUT, password)
        logger.info(f"Введены данные для логина: Email={email}")

    def submit_login(self):
        self.click(self.LOGIN_BUTTON)
        logger.info("Нажата кнопка 'Login'")