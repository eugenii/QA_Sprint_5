# Файл с локаторами для тестов.
from selenium.webdriver.common.by import By


class TestRegistrationPageLocators:
    """Локаторы для страницы регистрации."""
    # Поле имя.
    NAME_ENTRY_FIELD = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    # Поле email.
    EMAIL_ENTRY_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    # Поле пароль.
    PASSWORD_ENTRY_FIELD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    # Кнопка "зарегистрироваться".
    REGISTRY_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')


class TestLoginButtonLocators:
    """Локаторы для  логина.кнопок входа."""

    # Кнопка "Bойти в аккаунт" на главной стр.
    ENTER_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')
    # "кнопка" Личный кабинет".
    PERSONAL_CAB_PAR = (By.XPATH, '//a/p[text()="Личный Кабинет"]')
    # "кнопка" Профиль".
    PROFILE_BUTTON = (By.XPATH, '//a[text()="Профиль"]')
    # "кнопка" Войти на стр. регистрации.
    LOGIN_FROM_REGISTRATION_PAR = (By.XPATH, '//p[text()="Уже зарегистрированы?"]/a[text()="Войти"]')
    # "кнопка" Войти на стр. восстановления.
    LOGIN_FROM_RECOVERY_PAR = (By.XPATH, '//p[text()="Вспомнили пароль?"]/a[text()="Войти"]')
    # "кнопка" Войти на стр. восстановления.
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Войти"]')


class TestEnter:
    """Локаторы полей для входа в аккаунт."""

    # Поле для email.
    ENTER_EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    # Поле ввода пароля.
    ENTER_PASSWORD_FIELD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    # Кнопка "Войти".
    QUIT_BUTTON = (By.XPATH, '//button[text()="Выход"]')

class TestMovesFromPersonalCab:
    """Локаторы для переходов из личного кабинета."""
    
    # Кнопка "Конструктор".
    CONSTRUCTOR_LABEL = (By.XPATH, '//p[text()="Конструктор"]')
    # Кнопка "Лента заказов".
    ORDERS_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    # Логотип Stella Burgers.
    STELLAR_LOGO = (By.XPATH, '//div[contains(@class, "AppHeader_header__logo__2D0X2")]')
    # Кнопка "Выход".
    QUIT_LABEL = (By.XPATH, '//button[text()="Выход"]')


class TestScrollElements:
    """Локаторы для скроллинга."""

    # Кнопка "Булки".
    BULKI_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG") and .//span[text()="Булки"]]')
    # Кнопка "Соусы".
    SAUCES_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG") and .//span[text()="Соусы"]]')
    # Кнопка "Начинки".
    STICKS_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG") and .//span[text()="Начинки"]]')
