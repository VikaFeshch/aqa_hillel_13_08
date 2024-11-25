from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TrackNP:
    def __init__(self):
        self.locators = [
            (By.XPATH, '//input[contains(@class,"track__form-group-input")]'),
            (By.ID, "np-number-input-desktop-btn-search-en"),
        ]

    def __call__(self, driver):
        try:
            for locator in self.locators:
                el = WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))
                return el.is_displayed()
        except:
            return False