# config.py

# --- Настройки WebDriver ---
BROWSER = "edge"   # варианты: "chrome",  "edge"
IMPLICIT_WAIT = 10
PAGE_LOAD_TIMEOUT = 20

# --- Основные URL ---
BASE_URL = "https://automationexercise.com"
LOGIN_URL = f"{BASE_URL}/login"

# --- валидные ---
VALID_USER = {
    "email": f"test_user_0006@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "password": "password123",
    "address": "123 Main Street",
    "city": "Anytown",
    "state": "Alaska",
    "zipcode": "99501",
    "country": "United States",
    "phone": "1234567890"
}
# --- невалидные ---
INVALID_USER = {
    "email": "invalid_email.com",  # без @
    "first_name": "BadUser"
}

LOG_FILE = "registration.log"
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"