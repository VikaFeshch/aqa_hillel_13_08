from lesson_27.src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

# class MainPageLocators:
#     GUEST_LOGIN_LINK = (By.CSS_SELECTOR, "button.header-link.-guest")

class MainPage(BasePage):
    GUEST_LOGIN_LINK = (By.CSS_SELECTOR, "button.header-link.-guest")

    def click_guest_login(self):
        self.actions.click(self.GUEST_LOGIN_LINK)