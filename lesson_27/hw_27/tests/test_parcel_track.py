from lesson_27.hw_27.src.pages.np_tracking_page import TrackNPPage
from lesson_27.hw_27.tests.base_test import BaseTest


class TestParcelTracking(BaseTest):
    def test_parcel_tracking(self, driver):
        self.open_page(driver)
        tracking_page = TrackNPPage(driver)
        parcel = "20451043783256"
        tracking_page.check_parsel_number(parcel)
        tracking_page.assert_result()