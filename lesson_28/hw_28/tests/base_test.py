from selenium.webdriver.remote.webdriver import WebDriver

from lesson_28.hw_28.src.pages.main_page import MainPage



class BaseTest:

    def login_as_guest(self, driver: WebDriver, auto_config: dict):
        main_page = MainPage(driver, auto_config)
        main_page.open()
        main_page.click_guest_login()

    def login(self, username: str, password: str):
        pass

    def sign_up_window(self, driver: WebDriver, auto_config: dict):
        main_page = MainPage(driver, auto_config)
        main_page.open()
        main_page.click_sign_up()

