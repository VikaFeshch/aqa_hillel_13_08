import time

from lesson_28.hw_28.src.models.sign_up_models import UserForSignUp
from lesson_28.hw_28.src.pages.garage_page import GaragePage
from lesson_28.hw_28.src.pages.sign_up_modal_window import SignUpModalWindow
from lesson_28.hw_28.tests.base_test import BaseTest

class TestRegUser(BaseTest):
    """Test Register window"""

    def test_reg_user(self, driver, auto_config):

        # Open sign up window
        self.sign_up_window(driver, auto_config)

        # Register user
        signup_w = SignUpModalWindow(driver, auto_config)
        reg_user = UserForSignUp()
        signup_w.sign_up(reg_user, 5)

        # Verify added user
        garage_page = GaragePage(driver, auto_config)
        assert garage_page.wait_button_add_car()


