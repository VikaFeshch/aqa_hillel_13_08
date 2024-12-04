
from lesson_28.src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    GUEST_LOGIN_LINK = (By.CSS_SELECTOR, "button.header-link.-guest")
    SIGN_IN = (By.CSS_SELECTOR, "button.header_signin")
    SIGN_UP = (By.CSS_SELECTOR, "button.btn-primary")


    def open(self):
        self.driver.get(self.base_url)

    def click_guest_login(self):
        self.actions.click(self.GUEST_LOGIN_LINK)

    def click_sign_in(self):
        self.actions.click(self.SIGN_IN)

    def click_sign_up(self):
        self.actions.click(self.SIGN_UP)

