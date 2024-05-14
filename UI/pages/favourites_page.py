from .base_page import BasePage
from .locators import FavoritesPageLocators, HeaderLocators

class FavoritesPage(BasePage):
    def go_to_product_page():
        link = self.browser.find_element(*FavoritesPageLocators.PRODUCT_LINK)
        link.click()

    def is_product_in_favorites(self, product_name):
        favorites_page_product_name = self.browser.find_element(*FavoritesPageLocators.PRODUCT_NAME)
        if favorites_page_product_name.text == product_name:
            return True
        else: 
            return False
