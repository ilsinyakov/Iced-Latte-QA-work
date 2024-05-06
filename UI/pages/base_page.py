import re

from selenium.common.exceptions import NoSuchElementException, \
                                       ElementClickInterceptedException, \
                                       ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators

class BasePage:    

    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # turn on implicitly wait   
    
    def add_product_to_cart(self):
        button = self.browser.find_element(*BasePageLocators.ADD_TO_CART_BUTTON)
        button.click()
    
    def add_product_2_to_cart(self):
        button = self.browser.find_element(*BasePageLocators.ADD_TO_CART_BUTTON_2)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*BasePageLocators.PRODUCT_NAME).text
    
    def get_product_price(self):
        product_price_element = self.browser.find_element(*BasePageLocators.PRODUCT_PRICE).text
        return float(product_price_element[1:])
    
    def get_product_rating(self):
        product_rating = self.browser.find_element(*BasePageLocators.PRODUCT_RATING).text
        return product_rating
    
    def get_product_reviews(self):
        product_reviews_element = self.browser.find_element(*BasePageLocators.PRODUCT_REVIEWS).text
        pattern = re.compile(r'\b\d+\b')
        product_reviews = pattern.findall(product_reviews_element)
        return product_reviews[0]

    def get_product_weight(self):
        product_weight_element = self.browser.find_element(*BasePageLocators.PRODUCT_WEIGHT).text
        pattern = re.compile(r'\b\d+\b')
        product_weight = pattern.findall(product_weight_element)
        return product_weight[0]

    def go_to_cart_page(self):
        link = self.browser.find_element(*BasePageLocators.CART_LINK)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_product_page(self):
        link = self.browser.find_element(*BasePageLocators.PRODUCT_LINK)
        link.click()

    def go_to_profile_page(self):
        link = self.browser.find_element(*BasePageLocators.PROFILE_LINK)
        link.click()
    
    # check that amount on cart icon changed after adding product to cart
    def is_change_cart_icon(self, amount):
        cart_icon = self.browser.find_element(*BasePageLocators.CART_ICON)
        if cart_icon.text == amount:
            return True
        else: 
            return False

    # check that the element is clickable
    def is_element_clickable(self, how, what):
        try:
            self.browser.find_element(how, what)
        except ElementClickInterceptedException or ElementNotInteractableException:
            return False
        return True    

    # check that the element is present on the page
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True    
    
    # open page
    def open(self):
        self.browser.get(self.url)    

    # check that login link is present on the page
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"    
    