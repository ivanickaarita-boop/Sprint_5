from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.urls import Urls
from web_locators.locators import (
    MainPageLocators,
    LoginPageLocators,
    RegisterPageLocators,
    ForgotPasswordPageLocators
)


class TestLogin:

    def test_login_from_main_page_login_button(self, driver, registered_user):
        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()

        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(registered_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(registered_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )

        assert driver.current_url == Urls.MAIN_PAGE

    def test_login_from_profile_button(self, driver, registered_user):
        driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()

        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(registered_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(registered_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )

        assert driver.current_url == Urls.MAIN_PAGE

    def test_login_from_registration_form(self, driver, registered_user):
        driver.get(Urls.REGISTER_PAGE)

        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()

        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(registered_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(registered_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )

        assert driver.current_url == Urls.MAIN_PAGE

    def test_login_from_forgot_password_form(self, driver, registered_user):
        driver.get(Urls.FORGOT_PASSWORD_PAGE)

        driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()

        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(registered_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(registered_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )

        assert driver.current_url == Urls.MAIN_PAGE