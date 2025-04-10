# Файл с локаторами для тестов.
from selenium.webdriver.common.by import By


class TestRegistrationPageLocators:
    """Локаторы для страницы регистрации."""

    NAME_ENTRY_FIELD = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    EMAIL_ENTRY_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_ENTRY_FIELD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    REGISTRY_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')


class TestURLs:
    """URL проверок."""

    MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"  # Гл. страница

    REGISTRATION_PAGE = "https://stellarburgers.nomoreparties.site/register"  # Стр. регистрации

    RECOVERY_PAGE = "https://stellarburgers.nomoreparties.site/forgot-password"  # Стр. восстановления

    FEED_PAGE = "https://stellarburgers.nomoreparties.site/feed"  # Стр. ленты

    LOGIN_PAGE = "https://stellarburgers.nomoreparties.site/login"

    PERSONAL_CAB_PAGE = "https://stellarburgers.nomoreparties.site/account/profile"


class TestLoginButtonLocators:
    """Локаторы для  логина.кнопок входа."""

    ENTER_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка войти в аккаунт на главной стр.
    
    PERSONAL_CAB_PAR = (By.XPATH, '//a/p[text()="Личный Кабинет"]')   # "кнопка" Личный кабинет "

    PROFILE_BUTTON = (By.XPATH, '//a[text()="Профиль"]')   # "кнопка" Профиль "
    
    LOGIN_FROM_REGISTRATION_PAR = (By.XPATH, '//p[text()="Уже зарегистрированы?"]/a[text()="Войти"]')   # "кнопка" Войти на стр. регистрации
    
    LOGIN_FROM_RECOVERY_PAR = (By.XPATH, '//p[text()="Вспомнили пароль?"]/a[text()="Войти"]')    # "кнопка" Войти на стр. восстановления
    
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Войти"]')


class TestEnter:
    """Локаторы полей для входа в аккаунт."""

    ENTER_EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    ENTER_PASSWORD_FIELD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    QUIT_BUTTON = (By.XPATH, '//button[text()="Выход"]')

class TestMovesFromPersonalCab:
    """Локаторы для переходов из личного кабинета."""

    CONSTRUCTOR_LABEL = (By.XPATH, '//p[text()="Конструктор"]')
    ORDERS_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    STELLAR_LOGO = (By.XPATH, '//div[contains(@class, "AppHeader_header__logo__2D0X2")]')
    QUIT_LABEL = (By.XPATH, '//button[text()="Выход"]')


class TestScrollElements:
    """Локаторы для скроллинга."""

    BULKI_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG") and .//span[text()="Булки"]]')
    SAUCES_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG") and .//span[text()="Соусы"]]')
    STICKS_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG") and .//span[text()="Начинки"]]')
