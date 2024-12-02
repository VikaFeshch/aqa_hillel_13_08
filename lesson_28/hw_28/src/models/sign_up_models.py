import random
import string
from dataclasses import dataclass

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@dataclass
class UserForSignUp:
    """SignUp object for sign_up_modal_window"""
    signup_name: str = "Vika"
    signup_lastname: str = "Fesh"
    signup_email: str = f"user_{random_string()}@test.com"
    signup_password: str = "123qweRTY"
    signupRepeatPassword: str = "123qweRTY"
