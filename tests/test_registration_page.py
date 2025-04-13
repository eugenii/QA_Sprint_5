import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..locators import TestRegistrationPageLocators as Locators
from ..urls import TestURLs
from ..management.helpers import createAuthPair


class TestRegistrationPage:
    """Тесты для страницы регистрации."""

    @pytest.mark.parametrize(
            'name, email, password, result, comm',
            [
                ["Eu", createAuthPair()[0], createAuthPair()[1], "Войти", "Неверная обработка данных регистрации"],
                ["", createAuthPair()[0], createAuthPair()[1], "Войти", "Неверная обработка при пустом имени"],
                ["Eu", createAuthPair()[0], createAuthPair(valid_password=False)[1], "Войти", "Неверная обработка при коротком пароле"],
                ["Eu", createAuthPair()[0], "", "Войти", "Неверная обработка при пустом пароле пароле"],
                ["Eu", createAuthPair(valid_email=False)[0], "", "Войти", "Неверная обработка неверном email"],
            ]
    )
    def test_registration_page(self, chrome, name, email, password, result, comm):

        chrome.get(TestURLs.REGISTRATION_PAGE)

        # Ожидаем появления полей
        name_element = WebDriverWait(chrome, 10).until(
            EC.presence_of_element_located(Locators.NAME_ENTRY_FIELD)
        )
        email_element = WebDriverWait(chrome, 5).until(
                EC.presence_of_element_located(Locators.EMAIL_ENTRY_FIELD)
        )
        password_element = WebDriverWait(chrome, 5).until(
                EC.presence_of_element_located(Locators.PASSWORD_ENTRY_FIELD)
        )
        registry_button = WebDriverWait(chrome, 5).until(
                EC.element_to_be_clickable(Locators.REGISTRY_BUTTON)
        )

        # Очищаем поля перед вводом новых данных
        name_element.clear()
        email_element.clear()
        password_element.clear()

        name_element.send_keys(name)
        email_element.send_keys(email)
        password_element.send_keys(password)

        registry_button.click()

        assert registry_button.text != result, comm

