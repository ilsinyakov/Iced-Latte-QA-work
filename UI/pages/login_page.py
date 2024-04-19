from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators

from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def go_to_registration_page(self):
        link = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        link.click()

    def login_existing_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button.click()

    # check that sort drop-down is not present on the page
    def is_dropdown_present(self):
        try:
            self.browser.find_element(*BasePageLocators.SORT_DROPDOWN)
        except NoSuchElementException:
            return False
        return True        
