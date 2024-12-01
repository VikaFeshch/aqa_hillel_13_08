from dataclasses import dataclass

@dataclass
class UserForSignUp:
    """SignUp object for sign_up_modal_window"""
    signup_name: str = "Vika"
    signup_lastname: str = "Fesh"
    signup_email: str = "vf@gmail.com"
    signup_password: str = "123qweRTY"
    signupRepeatPassword: str = "123qweRTY"

