import pytest
from allure import step, title, severity, story, severity_level
from time import sleep

from .pages.base_page import BasePage
from .pages.favorites_page import FavoritesPage
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .set_of_steps import login_user, remove_products_from_cart_and_favorites
from .configs import link


def test_remove_cart_favorites_user(browser):
    with step('Login user'):
        login_user(browser, link)
    with step('Remove products from the cart and favorites'):
        remove_products_from_cart_and_favorites(browser, link)
