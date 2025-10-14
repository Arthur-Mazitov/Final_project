from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, "No login in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, password, email):
        REGISTER_EMAIL = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        REGISTER_EMAIL.send_keys(email)
        REGISTER_PASSWORD = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        REGISTER_PASSWORD.send_keys(password)
        REGISTER_PASSWORD_CONFIRMATION = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRMATION)
        REGISTER_PASSWORD_CONFIRMATION.send_keys(password)
        SUBMIT_REGISTRATION = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION)
        SUBMIT_REGISTRATION.click()

