from .pages.cart_page import CartPage
from .pages.base_page import BasePage
from .configs import link, product_id

from allure import step, title, severity, story, severity_level
import pytest
from time import sleep


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
            sleep(2)
            assert page.is_cart_empty, 'Cart is not empty'
        with step('Go to Main Page from Empty Cart'):
            page.go_to_main_page()
            sleep(2)
            assert browser.current_url == link, 'Continue Shopping Button do not work'
    
    @title("Test Full Shopping Cart")
    def test_full_cart(self, browser):
        with step('Open Main Page'):
            page = BasePage(browser, link)
            page.open()
        with step('Get Product Name from Main Page'):
            main_page_product_name = page.get_product_name()
        with step('Add Product to Cart'):
            page.add_product_to_cart()
            sleep(3)
            assert page.is_change_cart_icon('1'), 'Cart icon is not change'
        with step('Go to Cart Page'):
            page.go_to_cart_page()
        with step('Assert added product is in the cart'):
            page = CartPage(browser, browser.current_url)
            sleep(3)
            page.is_product_in_cart(main_page_product_name), 'Product is not in the cart'
