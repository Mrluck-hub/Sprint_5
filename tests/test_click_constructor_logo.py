from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
import pytest

class TestContructor:
    
        @pytest.mark.parametrize("locator", [
                TestLocators.HEADER_CONSTRUCTOR_BUTTON, 
                TestLocators.HEADER_LOGO_BUTTON,
                ])
        def test_open_constructor_from_profile(self, driver, locator):        
                driver.get(self.URL)
                driver.find_element(*TestLocators.MAIN_LOGIN_BUTTON).click()
                driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys("VyacheslavMelnikov_38@yandex.ru")
                driver.find_element(*TestLocators.LOGIN_PASS_INPUT).send_keys("olegoleg1")
                driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON).click()
        
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.HEADER_CABINET_BUTTON)).click()
                WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))

                driver.find_element(*locator).click()

                assert driver.current_url.rstrip('/') == self.URL 