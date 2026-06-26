import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.urls import Urls
from data.data import UserData
from utils.generators import generate_email, generate_password
from web_locators.locators import LoginPageLocators, MainPageLocators, RegisterPageLocators


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--window-size=1300,1200')

    browser = webdriver.Chrome(options=options)
    browser.get(Urls.MAIN_PAGE)

    yield browser

    browser.quit()


@pytest.fixture
def registered_user(driver):
    email = generate_email()
    password = generate_password()

    driver.get(Urls.REGISTER_PAGE)

    driver.find_element(*RegisterPageLocators.NAME_FIELD).send_keys(UserData.NAME)
    driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 8).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
    )

    return {
        'email': email,
        'password': password
    }


@pytest.fixture
def logged_in_driver(driver, registered_user):
    driver.get(Urls.LOGIN_PAGE)

    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(registered_user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(registered_user['password'])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 8).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
    )

    return driver