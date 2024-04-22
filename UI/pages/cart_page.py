from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def is_cart_empty(self):
        not self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE)
    
    def go_to_main_page(self):
        button = self.browser.find_element(*CartPageLocators.CONTINUE_SHOPPING_BUTTON)
        button.click()
