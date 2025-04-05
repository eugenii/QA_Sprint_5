import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="function")
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit() 
