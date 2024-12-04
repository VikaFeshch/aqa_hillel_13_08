import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson_28.hw_28.src.models.sign_up_models import UserForSignUp
from lesson_28.src.pages.page_elements.left_menu import LeftMenu

from lesson_28.hw_28.src.pages.base_page import BasePage

class SignUpModalWindow(BasePage):
    def __init__(self, driver, qa_auto_config):
        super().__init__(driver, qa_auto_config)
        self.left_menu = LeftMenu(driver, qa_auto_config)

    # Modal window for sign up

    SIGN_UP_NAME = (By.ID, "signupName")
    SIGN_UP_LASTNAME = (By.ID, "signupLastName")
    SIGN_UP_EMAIL = (By.ID, "signupEmail")
    SIGN_UP_PASSWORD = (By.ID, "signupPassword")
    SIGN_UP_REPEAT_PASSWORD = (By.ID, "signupRepeatPassword")
    BUT_REGISTER = (By.XPATH, "//button[contains(@class, 'btn-primary') and text()='Register']")

    def open(self):
        self.driver.get(f"{self.base_url}")


    def sign_up(self, user_for_signup:UserForSignUp, wait_time: int = 5):
        """Registering user """
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(self.SIGN_UP_NAME))
        self.actions.fill(self.SIGN_UP_NAME, user_for_signup.signup_name)
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(self.SIGN_UP_LASTNAME))
        self.actions.fill(self.SIGN_UP_LASTNAME, user_for_signup.signup_lastname)
        self.actions.fill(self.SIGN_UP_EMAIL, user_for_signup.signup_email)
        self.actions.fill(self.SIGN_UP_PASSWORD, user_for_signup.signup_password)
        self.actions.fill(self.SIGN_UP_REPEAT_PASSWORD, user_for_signup.signupRepeatPassword)

        self.actions.click(self.BUT_REGISTER)

