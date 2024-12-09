from selenium import webdriver
import pytest
import time

from selenium.webdriver.common.by import By

from lesson_27.hw_27.src.pages.np_tracking_page import TrackNPPage



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://tracking.novaposhta.ua/#/uk")
    yield driver
    driver.quit()


class TestParcelTracking():
    def test_parcel_tracking(self, driver):
        # Set pages
        # tracking_page = TrackNPPage(driver)
        # time.sleep(1)
        # Tracking parcel
        field_inp = driver.find_element(By.XPATH,'//input[contains(@class,"track__form-group-input")]')
        btn = driver.find_element(By.ID, "np-number-input-desktop-btn-search-en")
        parcel = "20451043783256"
        field_inp.send_keys(parcel)
        btn.click()
        # tracking_page.parsel_number(parcel)
