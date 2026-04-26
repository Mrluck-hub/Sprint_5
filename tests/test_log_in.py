from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
import pytest
from urls import URL

class TestLogin:
    
    @pytest.mark.parametrize("entry_point_url,login_locator", [
        (URL, TestLocators.MAIN_LOGIN_BUTTON), 
        (URL, TestLocators.HEADER_CABINET_BUTTON), 
        (f"{URL}/register", TestLocators.REG_FORM_LOGIN_LINK), 
        (f"{URL}/forgot-password", TestLocators.FORGOT_PASS_LOGIN_LINK)
        ])
    
    def test_login_from_different_pages(self, driver, entry_point_url,login_locator):        
        driver.get(entry_point_url)
        driver.find_element(*login_locator).click()
        assert "/login" in driver.current_url
        driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys("VyacheslavMelnikov_38@yandex.ru")
        driver.find_element(*TestLocators.LOGIN_PASS_INPUT).send_keys("olegoleg1")
        driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON).click()        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.HEADER_CABINET_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        assert driver.find_element(*TestLocators.PROFILE_LOGIN_INPUT).get_attribute("value") == "VyacheslavMelnikov_38@yandex.ru"