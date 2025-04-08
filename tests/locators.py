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

'''
//*[@id="root"]/div/main/section[2]/div/button
/html/body/div/div/header/nav/a/p
//*[@id="root"]/div/main/div/div/p/a   восстановление
//*[@id="root"]/div/main/div/div/p/a  

'''