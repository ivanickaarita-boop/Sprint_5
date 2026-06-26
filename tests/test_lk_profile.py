from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.urls import Urls
from web_locators.locators import (
    MainPageLocators,
    ProfilePageLocators,
    LoginPageLocators,
)


class TestProfile:

    def test_click_profile_button_opens_profile_page(self, logged_in_driver):
        logged_in_driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()

        WebDriverWait(logged_in_driver, 8).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TEXT)
        )

        assert logged_in_driver.current_url == Urls.PROFILE_PAGE

    def test_click_constructor_button_from_profile_opens_main_page(self, logged_in_driver):
        logged_in_driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()

        WebDriverWait(logged_in_driver, 8).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TEXT)
        )

        logged_in_driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(logged_in_driver, 8).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )

        assert logged_in_driver.current_url == Urls.MAIN_PAGE

    def test_click_logo_from_profile_opens_main_page(self, logged_in_driver):
        logged_in_driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()

        WebDriverWait(logged_in_driver, 8).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TEXT)
        )

        logged_in_driver.find_element(*MainPageLocators.LOGO_BUTTON).click()

        WebDriverWait(logged_in_driver, 8).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )

        assert logged_in_driver.current_url == Urls.MAIN_PAGE

    def test_logout_from_profile_page(self, logged_in_driver):
        logged_in_driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()

        WebDriverWait(logged_in_driver, 8).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )

        logged_in_driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

        WebDriverWait(logged_in_driver, 8).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )

        assert logged_in_driver.current_url == Urls.LOGIN_PAGE