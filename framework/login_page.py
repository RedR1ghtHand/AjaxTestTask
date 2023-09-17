from .page import Page
from tests.buttons import ButtonsXpath


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        self.click_element('xpath', ButtonsXpath['LogIn'])
        self.find_element('xpath', ButtonsXpath['email_button_path']).send_keys(email)
        self.find_element('xpath', ButtonsXpath['password_button_path']).send_keys(password)
        self.click_element('xpath', ButtonsXpath['LogIn_from_LogIn'])
