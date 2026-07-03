from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def login(self, email, password):
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click(LoginPageLocators.LOGIN_BUTTON)