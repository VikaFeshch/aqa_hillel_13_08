from selenium.webdriver.remote.webdriver import WebDriver

from lesson_27.hw_27.src.pages.np_tracking_page import TrackNPPage



class BaseTest:

    def open_page(self, driver: WebDriver):
        url = "https://tracking.novaposhta.ua/#/uk"
        work_page = TrackNPPage(driver)
        work_page.open(url)

