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
            sleep(3)
        with step('Get product data from main page'):
            main_page_product_name = page.get_product_name()
            main_page_product_price = page.get_product_price()
            main_page_product_weight = page.get_product_weight()
            main_page_product_rating = page.get_product_rating()
            main_page_product_reviews = page.get_product_reviews()
        with step('Go to product page'):
            page.go_to_product_page()
            sleep(3)
            page = ProductPage(browser, browser.current_url)
        with step('Check product name'):            
            product_page_product_name = page.get_product_name()
            assert product_page_product_name == main_page_product_name, \
            'Product names is not equal on main and product pages'
        with step('Check product price'):
            product_page_product_price = page.get_product_price()
            assert product_page_product_price == main_page_product_price, \
            'Product price is not equal on main and product pages'
        with step('Check product weight'):
            product_page_product_weight = page.get_product_weight()
            assert product_page_product_weight == main_page_product_weight, \
            'Product weight is not equal on main and product pages'
        # ### . vs , ###
        # with step('Check product rating'):
        #     product_page_product_rating = page.get_product_rating()
        #     assert product_page_product_rating == main_page_product_rating, \
        #     'Product rating is not equal on main and product pages'
        with step('Check product reviews count'):
            product_page_product_reviews = page.get_product_reviews()
            assert product_page_product_reviews == main_page_product_reviews, \
            'Product reviews count is not equal on main and product pages'
