import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import TestLoginButtonLocators as Locators
from .locators import TestURLs as URLs
from .locators import TestEnter as TE
from .locators import TestMovesFromPersonalCab as Moves


class TestMovesFromPersonalCab:
    """Класс тестирования переходов из личного кабинета."""
    
    @pytest.mark.parametrize(
        'locator, url, comm',
        [
            [Moves.CONSTRUCTOR_LABEL, URLs.MAIN_PAGE, "переход с 'Конструктора не верен'"],
            [Moves.STELLAR_LOGO, URLs.MAIN_PAGE, "переход с 'Логотипа' не верен"],
            [Moves.QUIT_LABEL, URLs.LOGIN_PAGE, "Неверный переход с 'Выход'"]
        ]
    )
    def test_moves_from_personal_cab(self, chrome, login, locator, url, comm):
        """Тестирование переходов из личного кабинета."""
        
        # Вход в личный кабинет
        enter_button = WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((Locators.PERSONAL_CAB_PAR)))
        enter_button.click()

        target_button = WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((locator)))
        target_button.click()

        WebDriverWait(chrome, 5).until(EC.url_to_be(url))
        
        assert chrome.current_url == url, comm

        # Выходим из аккаунта
        enter_button.click()
        if 'login' not in chrome.current_url:
            quit_button = WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((Moves.QUIT_LABEL)))
            quit_button.click()

        