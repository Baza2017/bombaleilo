# pages/base_page.py

import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import config

# Настройка логгера
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format=config.LOG_FORMAT,
    filename=config.LOG_FILE,
    filemode='a'
)
logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config.PAGE_LOAD_TIMEOUT)

    def open(self, url):
        self.driver.get(url)
        logger.info(f"Открыта страница: {url}")

    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logger.exception(f"Элемент не найден по локатору: {locator}")
            raise

    def click(self, locator):
        element = self.find_element(locator)
        element.click()
        time.sleep(2)  # Для демонстрации, можно убрать в продакшене

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)
        time.sleep(2)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text