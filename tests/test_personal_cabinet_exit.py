from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

def test_personal_cabinet(self, driver):
    driver.get(f"{self.URL}/login")
    driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys("VyacheslavMelnikov_38@yandex.ru")
    driver.find_element(*TestLocators.LOGIN_PASS_INPUT).send_keys("olegoleg1")
    driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON).click()
    
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.HEADER_CABINET_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.url_contains("/account/profile"))
    assert "/account/profile" in driver.current_url

def test_personal_cabinet_is_exit(self, driver):   
    driver.get(f"{self.URL}/login")
    driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys("VyacheslavMelnikov_38@yandex.ru")
    driver.find_element(*TestLocators.LOGIN_PASS_INPUT).send_keys("olegoleg1")
    driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON).click()
    
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.HEADER_CABINET_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.url_contains("/account/profile"))
    
    driver.find_element(*TestLocators.HEADER_CABINET_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.PROFILE_EXIT_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    assert "/login" in driver.current_url