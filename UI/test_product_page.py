import pytest
from allure import step, title, severity, story, severity_level
from time import sleep

from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .set_of_steps import login_user
from .configs import link


@story("Product Page")
# @allure.description("")
# @allure.tag("")
@severity(severity_level.CRITICAL)
class TestPruductPage:
    @title("Test main page product's data is equal product page")
    def test_product_data(self, browser):
        with step('Open main page'):            
            page = BasePage(browser, link)
            page.open()
        with step('Get product data from main page'):
            main_page_product_name = page.get_product_name()
            main_page_product_price = page.get_product_price()
            main_page_product_weight = page.get_product_weight()
            main_page_product_rating = page.get_product_rating()
        with step('Go to product page'):
            page.go_to_product_page()
            page = ProductPage(browser, browser.current_url)
        with step('Check product name'):            
            assert product_page_product_name == page.get_product_name(), \
            'Product names is not equal on main and product pages'
        with step('Check product price'):
            assert main_page_product_price == page.get_product_price(), \
            'Product price is not equal on main and product pages'
        with step('Check product weight'):
            assert main_page_product_weight == page.get_product_weight(), \
            'Product weight is not equal on main and product pages'
        with step('Check product rating'):
            assert main_page_product_rating == page.get_product_rating(), \
            'Product rating is not equal on main and product pages'
        
        

