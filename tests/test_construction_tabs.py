from locators import TestLocators
import pytest
from urls import URL

class TestTabs:

    @pytest.mark.parametrize("locator", [
        TestLocators.TAB_FILLINGS,
        TestLocators.TAB_BUNS,
        TestLocators.TAB_SAUCES
        ])
    def test_construction_tabs(self, driver, locator):
        driver.get(URL)
        driver.find_element(*locator).click()
    
        assert "current" in driver.find_element(*locator).get_attribute("class")