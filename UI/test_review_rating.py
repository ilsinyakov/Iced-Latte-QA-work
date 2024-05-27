from allure import step, title, severity, story, severity_level
from time import sleep
import pytest

from .pages.base_page import BasePage
from .pages.favorites_page import FavoritesPage
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .set_of_steps import login_user, delete_old_review
from .configs import link


@story("Review, Rating")
# @allure.description("")
# @allure.tag("")
@severity(severity_level.NORMAL)
class TestReviewRating:
    @pytest.mark.skip
    def test_add_review_guest(self, browser):
        with step('Open main page'):            
                page = BasePage(browser, link)
                page.open()
                sleep(2)  # waiting is mandatory (do not remove)
        with step('Go to product page'):
            page.go_to_product_page()
            sleep(2)  # waiting is mandatory (do not remove)
            page = ProductPage(browser, browser.current_url)
        with step('Push "Add a review button"'):
            page.add_review()
            page = LoginPage(browser, browser.current_url)            
            assert page.is_login_page(), 'The guest was not redirected to the login page'        
    def test_add_delete_review_user(self, browser):
        with step('Login user'):
            login_user(browser, link)
        with step('Delete old review'):
            delete_old_review(browser, link)
            