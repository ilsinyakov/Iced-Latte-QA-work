from allure import step, title, severity, story, severity_level
from time import sleep
import pytest

from .pages.base_page import BasePage
from .pages.favorites_page import FavoritesPage
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .set_of_steps import login_user, delete_old_review
from .configs import link, first_name
from data.text_review import parameterize_text_review_positive


@story("Review, Rating")
# @allure.description("")
# @allure.tag("")
@severity(severity_level.NORMAL)
class TestReviewRating:
    @pytest.mark.skip
    def test_add_review_guest(self, browser):
        with step('Open main page'):            
                main_page = BasePage(browser, link)
                main_page.open()
                sleep(2)  # waiting is mandatory (do not remove)
        with step('Go to product page'):
            main_page.go_to_product_page()
            sleep(2)  # waiting is mandatory (do not remove)
            product_page = ProductPage(browser, browser.current_url)
        with step('Click "Add a review" button'):
            product_page.click_add_review()
            login_page = LoginPage(browser, browser.current_url)            
            assert login_page.is_login_page(), 'The guest was not redirected to the login page'     

    @pytest.mark.skip
    def test_add_and_delete_review_user(self, browser):
        with step('Login user'):
            login_user(browser, link)
        with step('Delete old review'):
            delete_old_review(browser, link)
        with step('Get actual rating'):
            product_page = ProductPage(browser, browser.current_url)
            old_rating, old_reviews_amount = product_page.get_actual_rating()
        with step('Add review and rating'):
            product_page.click_add_review()
            product_page.set_rating()
            review_text = "It's a very good coffee"
            product_page.fill_review(review_text)
            counter = product_page.get_review_symbols_counter()
            assert counter == len(review_text), 'Counter does not work'
            product_page.submit_review()
            assert product_page.get_review_author() == first_name, \
                f'Review author {first_name} is not present'
            new_rating, new_reviews_amount = product_page.get_actual_rating()
            assert new_rating == round((old_rating * old_reviews_amount + 2) 
                                        / (old_reviews_amount + 1), 1), \
                'New rating is not correct'            
            assert new_reviews_amount == product_page.get_reviews_amount(), \
                'Review amount is not correct'
        with step('Delete review'):
            product_page.delete_review()
            new_rating, new_reviews_amount = product_page.get_actual_rating()
            assert new_rating == old_rating, 'New rating is not correct'
            assert new_reviews_amount == product_page.get_reviews_amount() \
                   and new_reviews_amount == old_reviews_amount, \
                'Review amount is not correct'
    
    @pytest.mark.parametrize('review_text', parameterize_text_review_positive)
    def test_add_review_parametrize(self, browser, review_text):
        print(review_text)
