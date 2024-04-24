from .pages.cart_page import CartPage
from .pages.base_page import BasePage
from .set_of_steps import login_user
from .configs import link, email, password

from allure import step, title, severity, story, severity_level
import pytest
from time import sleep


@story("Cart Page")
# @allure.description("")
# @allure.tag("")
@severity(severity_level.CRITICAL)
class TestCart:
    
    # ------------- GUEST ---------------

    @title("Test Empty Shopping Cart. User is not logged in")
    # @pytest.mark.skip
    def test_guest_empty_cart(self, browser):
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
    
    @title("Test Full Shopping Cart. User is not logged in")
    # @pytest.mark.skip
    def test_guest_full_cart(self, browser):
        with step('Open Main Page'):
            page = BasePage(browser, link)
            page.open()
        with step('Get Product Name from Main Page'):
            main_page_product_name = page.get_product_name()
        with step('Add Product to Cart'):
            page.add_product_to_cart()
            sleep(3)
            main_page_product_price = float(page.get_product_price()[1:])
            assert page.is_change_cart_icon('1'), 'Cart icon is not change'
        with step('Go to Cart Page'):
            page.go_to_cart_page()
        with step('Assert added product is in the cart'):
            page = CartPage(browser, browser.current_url)
            sleep(3)
            cart_page_product_price = float(page.get_product_cost()[1:])
            assert page.is_product_in_cart(main_page_product_name), 'Product is not in the cart'
            assert main_page_product_price == cart_page_product_price, 'Main Page Price are not Equal Cart Page Price'
        '''with step('Click on Plus Button'):            
            page.click_plus_button()
            sleep(3)
            assert page.is_change_cart_icon('2'), 'Cart icon is not change'
            assert page.is_change_amount('2'), 'Amount is not change'
        with step('Click on Minus Button'):
            page.click_minus_button()
            sleep(3)
            assert page.is_change_cart_icon('1'), 'Cart icon is not change'
            assert page.is_change_amount('1'), 'Amount is not change'
        '''
        with step('Remove Product from the Cart'):
            page.remove_product()
            sleep(3)
            assert page.is_cart_empty, 'Cart is not empty'
    
    @title("Test the Cost in the Shopping Cart. User is not logged in")
    def test_guest_cart_cost(self, browser):
        with step('Open Main Page'):
            page = BasePage(browser, link)
            page.open()
        with step('Add Product 1 to Cart'):
            page.add_product_to_cart()            
            sleep(3)
            assert page.is_change_cart_icon('1'), 'Cart icon is not change'
        with step ('Add Product 2 to Cart'):
            page.add_product_2_to_cart()            
            sleep(3)
            assert page.is_change_cart_icon('2'), 'Cart icon is not change'
        with step('Go to Cart Page'):
            page.go_to_cart_page()
            page = CartPage(browser, browser.current_url)
            sleep(3)
            cart_page_product_price = float(page.get_product_cost()[1:])
            cart_page_product_2_price = float(page.get_product_2_cost()[1:])        
        with step('Assert Subtotal Cost is Equal Sum of Prices'):
            subtotal = float(page.get_subtotal()[1:])
            assert (cart_page_product_price + cart_page_product_2_price) == subtotal
        '''with step('Click on Plus Button by Product 1'):
            page.click_plus_button()
            sleep(3)
            cart_page_product_cost = float(page.get_product_cost()[1:])
            assert cart_page_product_cost == cart_page_product_price * 2, 'Cost != Price * Amount'
        with step('Click on Plus Button by Product 2'):
            page.click_plus_2_button()
            sleep(3)
            cart_page_product_2_cost = float(page.get_product_2_cost()[1:])
            subtotal = float(page.get_subtotal()[1:])
            assert cart_page_product_2_cost == cart_page_product_2_price * 2, 'Cost != Price * Amount'
            assert subtotal == (cart_page_product_price * 2 + cart_page_product_2_price * 2)
        '''
    # ------------- USER ---------------

    @title("Test Empty Shopping Cart. User is logged in")
    # @pytest.mark.skip
    def test_user_empty_cart(self, browser):        
        with step('Login User'):
            browser.delete_all_cookies()
            login_user(browser, link)
        with step('Go to Cart Page'):
            page = BasePage(browser, link)
            page.go_to_cart_page()
        with step('Assert Cart is Empty'):
            page = CartPage(browser, browser.current_url)
            sleep(2)
            assert page.is_cart_empty, 'Cart is not empty'
        with step('Go to Main Page from Empty Cart'):
            page.go_to_main_page()
            sleep(2)
            assert browser.current_url == link, 'Continue Shopping Button do not work'
    
    @title("Test Full Shopping Cart. User is logged in")
    # @pytest.mark.skip
    def test_user_full_cart(self, browser):
        with step('Login User'):
            login_user(browser, link)
        with step('Get Product Name from Main Page'):
            page = BasePage(browser, link)
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
            assert page.is_change_amount('2'), 'Amount is not change'
        with step('Click on Minus Button'):
            page.click_minus_button()
            sleep(3)
            assert page.is_change_cart_icon('1'), 'Cart icon is not change'
            assert page.is_change_amount('1'), 'Amount is not change'
        '''
        with step('Remove Product from the Cart'):
            page.remove_product()
            sleep(3)
            assert page.is_cart_empty, 'Cart is not empty'
    
    @title("Test the Cost in the Shopping Cart. User is logged in")
    def test_user_cart_cost(self, browser):
        with step('Login User'):
            login_user(browser, link)
        with step('Add Product 1 to Cart'):
            page = BasePage(browser, link)
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
            sleep(3)
            cart_page_product_price = float(page.get_product_cost()[1:])
            cart_page_product_2_price = float(page.get_product_2_cost()[1:])
        with step('Assert Main Page Prices are Equal Cart Page Prices'):
            assert main_page_product_price == cart_page_product_price and \
                   main_page_product_2_price == cart_page_product_2_price, \
                   'Main Page Prices are not Equal Cart Page Prices'
        with step('Assert Subtotal Cost is Equal Sum of Prices'):
            subtotal = float(page.get_subtotal()[1:])
            assert (cart_page_product_price + cart_page_product_2_price) == subtotal
        '''with step('Click on Plus Button by Product 1'):
            page.click_plus_button()
            sleep(3)
            cart_page_product_cost = float(page.get_product_cost()[1:])
            assert cart_page_product_cost == cart_page_product_price * 2, 'Cost != Price * Amount'
        with step('Click on Plus Button by Product 2'):
            page.click_plus_2_button()
            sleep(3)
            cart_page_product_2_cost = float(page.get_product_2_cost()[1:])
            subtotal = float(page.get_subtotal()[1:])
            assert cart_page_product_2_cost == cart_page_product_2_price * 2, 'Cost != Price * Amount'
            assert subtotal == (cart_page_product_price * 2 + cart_page_product_2_price * 2)
        '''  
