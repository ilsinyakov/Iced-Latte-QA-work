from .pages.cart_page import CartPage
from .pages.base_page import BasePage
from .configs import link

from allure import step, title, severity, story, severity_level
import pytest
from time import sleep


@story("Cart Page")
# @allure.description("")
# @allure.tag("")
@severity(severity_level.CRITICAL)
class TestCart:
    @title("Test Empty Shopping Cart")
    @pytest.mark.skip
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
    @pytest.mark.skip
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
            assert page.is_product_in_cart(main_page_product_name), 'Product is not in the cart'
        '''with step('Click on Plus Button'):            
            page.click_plus_button()
            sleep(3)
            assert page.is_change_cart_icon('2'), 'Cart icon is not change'
        with step('Click on Minus Button'):
            page.click_minus_button()
        '''
        with step('Remove Product from the Cart'):
            page.remove_product()
            sleep(3)
            assert page.is_cart_empty, 'Cart is not empty'
    
    @title("Test the Cost in the Shopping Cart")
    def test_cart_cost(self, browser):
        with step('Open Main Page'):
            page = BasePage(browser, link)
            page.open()
        with step('Add Product 1 to Cart'):
            page.add_product_to_cart()
            main_page_product_price = float(page.get_product_price()[1:])
            sleep(3)
            assert page.is_change_cart_icon('1'), 'Cart icon is not change'
        with step ('Add Product 2 to Cart'):
            page.add_product_2_to_cart()
            main_page_product_2_price = float(page.get_product_2_price()[1:])
            sleep(3)
            assert page.is_change_cart_icon('2'), 'Cart icon is not change'
        with step('Go to Cart Page'):
            page.go_to_cart_page()
            page = CartPage(browser, browser.current_url)
            cart_page_product_price = float(page.get_product_price()[1:])
            cart_page_product_2_price = float(page.get_product_2_price()[1:])
        with step('Assert Main Page Prices are Equal Cart Page Prices'):
            assert main_page_product_price == cart_page_product_price and \
                   main_page_product_2_price == cart_page_product_2_price, \
                   'Main Page Prices are not Equal Cart Page Prices'
        with step('Assert Subtotal Cost is Equal Sum of Prices'):
            subtotal = float(page.get_subtotal())
            assert (cart_page_product_price + cart_page_product_2_price) == subtotal
