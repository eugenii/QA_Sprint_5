# Файл с локаторами для тестов.
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistrationPageLocators:
    """Локаторы для страницы регистрации."""

    NAME_ENTRY_FIELD = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    EMAIL_ENTRY_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_ENTRY_FIELD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    REGISTRY_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')
