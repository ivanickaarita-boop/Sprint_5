from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locators import MainPageLocators


class TestConstructor:

    def test_click_sauces_tab(self, driver):
        driver.find_element(*MainPageLocators.SAUCES_SECTION_BUTTON).click()

        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(MainPageLocators.SAUCES_HEADER)
        )

        assert driver.find_element(*MainPageLocators.SAUCES_HEADER).is_displayed()

    def test_click_fillings_tab(self, driver):
        driver.find_element(*MainPageLocators.FILLINGS_SECTION_BUTTON).click()

        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(MainPageLocators.FILLINGS_HEADER)
        )

        assert driver.find_element(*MainPageLocators.FILLINGS_HEADER).is_displayed()

    def test_click_buns_tab(self, driver):
        driver.find_element(*MainPageLocators.SAUCES_SECTION_BUTTON).click()

        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(MainPageLocators.SAUCES_HEADER)
        )

        driver.find_element(*MainPageLocators.BUNS_SECTION_BUTTON).click()

        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_HEADER)
        )

        assert driver.find_element(*MainPageLocators.BUNS_HEADER).is_displayed()