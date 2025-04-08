import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .tests.locators import TestLoginButtonLocators as Locators
from .tests.locators import TestEnter as TE



@pytest.fixture(scope="function")
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit() 


@pytest.fixture(scope="function")
def login(chrome):
    email_element = WebDriverWait(chrome, 5).until(
        EC.presence_of_element_located((TE.ENTER_EMAIL_FIELD))
    )
    password_element = WebDriverWait(chrome, 5).until(
        EC.presence_of_element_located((TE.ENTER_PASSWORD_FIELD))
    )
    email_element.send_keys('eu@gmail.com')
    password_element.send_keys('123456Q')
    button = WebDriverWait(chrome, 5).until(
        EC.element_to_be_clickable((Locators.SUBMIT_BUTTON))
        )
    button.click()
