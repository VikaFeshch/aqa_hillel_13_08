from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from lesson_27.hw_27.src.pages.base_page import BasePage
from lesson_27.hw_27.src.custom_expected_conditions import TrackNP


class TrackNPPage(BasePage):
    # Page for parsel tracking
    URL = "https://tracking.novaposhta.ua/#/uk"

    PARCEL_NUMBER_INPUT = (By.XPATH, '//input[contains(@class,"track__form-group-input")]')
    SEARCH_BTN = (By.ID, "np-number-input-desktop-btn-search-en")
    CHECK_RESULT = (By.XPATH, '//div[@class="header__status-text"]')



    def check_parsel_number(self, parsel_number: str, wait_time: int = 5):
        """Inputting number of parcel for searching"""
        self.actions.fill(self.PARCEL_NUMBER_INPUT, parsel_number)

        self.actions.click(self.SEARCH_BTN)
        WebDriverWait(self.driver, wait_time).until(TrackNP())

    def assert_result(self):
        actual_text = self.actions.find(self.CHECK_RESULT).text
        expected_text = "Отримана"

        assert actual_text == expected_text, f"Expected {expected_text}, but got '{actual_text}'"