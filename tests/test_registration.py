from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from urls import URL

class TestRegistration:
    
    def test_registration_success(self, driver):
        driver.get(f"{URL}/register")
        driver.find_element(*TestLocators.REG_NAME_INPUT).send_keys("Vyacheslav")
        driver.find_element(*TestLocators.REG_EMAIL_INPUT).send_keys("VyacheslavMelnikov_38@yandex.ru")
        driver.find_element(*TestLocators.REG_PASS_INPUT).send_keys("olegoleg1")
        driver.find_element(*TestLocators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    def test_registration_short_password_error(self, driver):
        driver.get(f"{URL}/register")
        driver.find_element(*TestLocators.REG_PASS_INPUT).send_keys("12345")
        driver.find_element(*TestLocators.REG_BUTTON).click()
        error = driver.find_element(*TestLocators.REG_ERROR_MESSAGE)
        assert error.text == "Некорректный пароль"