from .base_page import BasePage
from .locators import EditProfilePageLocators


class EditProfilePage(BasePage):
    def change_email(self, new_email):
        email_field = self.browser.find_element(*EditProfilePageLocators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(new_email)

    def change_first_name(self, new_first_name):
        first_name_field = self.browser.find_element(*EditProfilePageLocators.FIRST_NAME_FIELD)
        first_name_field.clear()
        first_name_field.send_keys(new_first_name)

    def change_last_name(self, new_last_name):
        last_name_field = self.browser.find_element(*EditProfilePageLocators.LAST_NAME_FIELD)
        last_name_field.clear()
        last_name_field.send_keys(new_last_name)

    def save_change(self):
        save_change_button = self.browser.find_element(*EditProfilePageLocators.SAVE_CHANGE_BUTTON)
        save_change_button.click()
    
    def is_error_message_present(self, error_message):
        message_empty_nonlatin = self.browser.find_element(*EditProfilePageLocators.EMPTY_NONLATIN_MESSAGE)
        message_server_error = self.browser.find_element(*EditProfilePageLocators.SERVER_ERROR_MESSAGE)
        if (message_empty_nonlatin.text in error_message) or (message_server_error.text in error_message):
            return True
        else:
            return False

'''    def is_success_message_present(self, success_message):
        message_element = self.browser.find_element(*EditProfilePageLocators.SUCCESS_MESSAGE)
        if message_element.text == success_message:
            return True
        else:
            return False
'''
