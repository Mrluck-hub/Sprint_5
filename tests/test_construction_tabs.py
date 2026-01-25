from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

def test_constructor_tabs_sauces(self, driver):
    driver.get(self.URL)
    driver.find_element(*TestLocators.TAB_SAUCES).click()
    assert "current" in driver.find_element(*TestLocators.TAB_SAUCES).get_attribute("class")
        
def test_constructor_tabs_fillings(self, driver):
    driver.get(self.URL)
    driver.find_element(*TestLocators.TAB_FILLINGS).click()
    assert "current" in driver.find_element(*TestLocators.TAB_FILLINGS).get_attribute("class")
    
def test_constructor_tabs_buns(self, driver):
    driver.get(self.URL)  
    driver.find_element(*TestLocators.TAB_BUNS).click()
    assert "current" in driver.find_element(*TestLocators.TAB_BUNS).get_attribute("class")