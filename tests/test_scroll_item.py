import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..urls import TestURLs as URLs
from ..locators import TestScrollElements as Scroll


class TestScrollItems:
    """Класс тестирования скроллинга."""
    
    @pytest.mark.parametrize(
        'locator, locator_first, comm',
        [
            [Scroll.BULKI_BUTTON, Scroll.SAUCES_BUTTON, "прокрутка до булок не сработала"],
            [Scroll.SAUCES_BUTTON, Scroll.STICKS_BUTTON, "прокрутка до соусов не сработала"],
            [Scroll.STICKS_BUTTON, Scroll.SAUCES_BUTTON, "прокрутка до начинки не сработала"]
        ]
    )
    def test_scroll_items(self, chrome, locator, comm):
        """Тестирование скроллинга."""
        
        chrome.get(URLs.MAIN_PAGE)

        first_touch_button = WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((locator_first)))
        first_touch_button.click()

        enter_button = WebDriverWait(chrome, 5).until(EC.element_to_be_clickable(locator))
        pre_class = enter_button.get_attribute("class")
        enter_button.click()
    

        # Wait for the class to change.
        WebDriverWait(chrome, 10).until(
            lambda d: enter_button.get_attribute("class") != pre_class
        )
        post_class = enter_button.get_attribute("class")
        
        assert pre_class != post_class, comm
        
