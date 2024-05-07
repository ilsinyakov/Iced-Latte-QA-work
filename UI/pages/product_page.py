import re

from .base_page import BasePage
from .locators import ProductPageLocators, HeaderLocators


class ProductPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def get_product_price(self):
        product_price_element = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).text
        pattern = r"[0-9.]"
        product_price = re.findall(pattern, product_price_element)
        return float("".join(product_price))
        
    def get_product_rating(self):
        product_rating = self.browser.find_element(*ProductPageLocators.PRODUCT_RATING).text
        return product_rating
    
    def get_product_reviews(self):
        product_reviews_element = self.browser.find_element(*ProductPageLocators.PRODUCT_REVIEWS).text
        pattern = re.compile(r'\b\d+\b')
        product_reviews = pattern.findall(product_reviews_element)
        return product_reviews[0]
    
    def get_product_weight(self):
        product_weight_element = self.browser.find_element(*ProductPageLocators.PRODUCT_WEIGHT).text
        pattern = re.compile(r'\b\d+\b')
        product_weight = pattern.findall(product_weight_element)
        return product_weight[0]
    
    def is_cart_page_link_present(self):
        self.is_element_present(*HeaderLocators.CART_LINK)

    def is_cart_page_link_clickable(self):
        self.is_element_clickable(*HeaderLocators.CART_LINK)    

    def is_favorites_page_link_present(self):
        self.is_element_present(*HeaderLocators.FAVORITES_PAGE_LINK)

    def is_favorites_page_link_clickable(self):
        self.is_element_clickable(*HeaderLocators.FAVORITES_PAGE_LINK)

    def is_login_page_link_present(self):
        self.is_element_present(*HeaderLocators.LOGIN_LINK)

    def is_login_page_link_clickable(self):
        self.is_element_clickable(*HeaderLocators.LOGIN_LINK)
    
    def is_main_page_link_present(self):
        self.is_element_present(*HeaderLocators.MAIN_PAGE_LINK)
    
    def is_main_page_link_clickable(self):
        self.is_element_clickable(*HeaderLocators.MAIN_PAGE_LINK)
    