import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import TestLoginButtonLocators as Locators
from .locators import TestEnter as TE
from .urls import TestURLs as URLs
from .management import data


@pytest.fixture(scope="function")
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit() 


@pytest.fixture(scope="function")
def login(chrome):
    """Enter to login page and login."""

    chrome.get(URLs.LOGIN_PAGE)
    email_element = WebDriverWait(chrome, 5).until(
        EC.presence_of_element_located((TE.ENTER_EMAIL_FIELD))
    )
    password_element = WebDriverWait(chrome, 5).until(
        EC.presence_of_element_located((TE.ENTER_PASSWORD_FIELD))
    )
    email_element.send_keys(data.login)
    password_element.send_keys(data.password)
    button = WebDriverWait(chrome, 5).until(
        EC.element_to_be_clickable((Locators.SUBMIT_BUTTON))
        )
    button.click()

    # Проверка успешности авторизации
    WebDriverWait(chrome, 10).until(
        EC.url_changes(URLs.LOGIN_PAGE)
    )

    # Финализатор: выходим из аккаунта после завершения теста
    yield
    try:
        pers_button = WebDriverWait(chrome, 5).until(
            EC.element_to_be_clickable((Locators.PERSONAL_CAB_PAR))
        )
        pers_button.click()

        quit_button = WebDriverWait(chrome, 5).until(
            EC.element_to_be_clickable((TE.QUIT_BUTTON))
        )
        quit_button.click()
    except Exception as e:
        print(f"Ошибка при выходе из аккаунта: {e}")
