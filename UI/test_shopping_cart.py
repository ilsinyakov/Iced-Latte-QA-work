from .pages.cart_page import CartPage
from .pages.base_page import BasePage
from .configs import link

from allure import step, title, severity, story, severity_level
import pytest


@story("Cart Page")
# @allure.description("")
# @allure.tag("")
@severity(severity_level.CRITICAL)
class TestCart:
    @title("Test Empty Shopping Cart")
    def test_empty_cart(self, browser):
        with step('Open Main Page'):
            page = BasePage(browser, link)
            page.open()
        with step('Go to Cart Page'):
            page.go_to_cart_page()
        with step('Assert Cart is Empty'):
            page = CartPage(browser, browser.current_url)
            assert page.is_cart_empty, 'Cart is not empty'
        with step('Go to Main Page from Empty Cart'):
            page.go_to_main_page()
            assert browser.current_url == link, 'Continue Shopping Button do not work'
    
    '''@title("Test Full Shopping Cart")
    def test_full_cart(browser):
        with step('Open Main Page'):
            page = BasePage(browser, link)
            page.open()
        with step('Add Product to Cart'):
            page.add_product_to_cart()
    '''
