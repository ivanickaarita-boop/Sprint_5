from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.urls import Urls
from data.data import UserData, ErrorMessages
from utils.generators import generate_email, generate_password
from web_locators.locators import LoginPageLocators, RegisterPageLocators


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(Urls.REGISTER_PAGE)

        driver.find_element(*RegisterPageLocators.NAME_FIELD).send_keys(UserData.NAME)
        driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(generate_password())
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )

        assert driver.current_url == Urls.LOGIN_PAGE

    def test_registration_with_incorrect_password_shows_error(self, driver):
        driver.get(Urls.REGISTER_PAGE)

        driver.find_element(*RegisterPageLocators.NAME_FIELD).send_keys(UserData.NAME)
        driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys('12345')
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        error_text = WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
        ).text

        assert error_text == ErrorMessages.INCORRECT_PASSWORD