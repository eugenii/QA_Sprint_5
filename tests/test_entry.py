import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..locators import TestLoginButtonLocators as Locators
from ..urls import TestURLs as URLs
from ..locators import TestEnter as TE
from ..management import data


class TestEntry:
    """Класс тестирования входа в аккаунт с различных страниц."""

    @pytest.mark.parametrize(
            'url, locator',
            [
                [URLs.MAIN_PAGE, Locators.ENTER_ACCOUNT_BUTTON],
                [URLs.REGISTRATION_PAGE, Locators.LOGIN_FROM_REGISTRATION_PAR],
                [URLs.RECOVERY_PAGE, Locators.LOGIN_FROM_RECOVERY_PAR],
                [URLs.MAIN_PAGE, Locators.PERSONAL_CAB_PAR],
            ]
    )
    def test_entry_from_different_pages(self, chrome, url, locator):
        """Тест входа в аккаунт с различных страниц."""
        chrome.get(url)
        button = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(locator))
        button.click()

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
        assert chrome.current_url == URLs.MAIN_PAGE


class TestEntryPersonalCab:
    """Класс тестирования входа в личный кабинет."""

    @pytest.mark.parametrize(
            'url',
            [
                URLs.MAIN_PAGE,
                URLs.REGISTRATION_PAGE,
                URLs.RECOVERY_PAGE,
                URLs.FEED_PAGE
            ]
    )
    def test_entry_personal_cab(self, chrome, login, url):
        """Тест входа в личный кабинет."""
        chrome.get(url)

        button = WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((Locators.PERSONAL_CAB_PAR)))
        button.click()

        WebDriverWait(chrome, 5).until(
            EC.presence_of_element_located(Locators.PROFILE_BUTTON)
        )

        assert 'account/profile' in chrome.current_url
