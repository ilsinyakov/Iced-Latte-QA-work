from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):    

    def go_to_main_page(self):
        button = self.browser.find_element(*CartPageLocators.CONTINUE_SHOPPING_BUTTON)
        button.click()

    def is_cart_empty(self):
        not self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE)
    
    #check that product name on main page equal product name on cart page
    def is_product_in_cart(self, main_page_product_name):
        cart_page_product_name = self.browser.find_element(*CartPageLocators.PRODUCT_NAME)
        if cart_page_product_name.text == main_page_product_name:
            return True
        else:
            return False   
