from .pages.base_page import BasePage
from .pages.cart_page import CartPage
from .pages.favorites_page import FavoritesPage
from .pages.login_page import LoginPage
from .pages.profile_page import ProfilePage

from .configs import email, password

from allure import step


def login_user(browser, link):
    with step('Open main page'):
        page = BasePage(browser, link)
        page.open()
    with step('Go to login page'):
        page.go_to_login_page()
    with step('Login existing user'):
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_existing_user(email, password)


def go_to_edit_profile_page(browser, link):    
    with step('Login existing user'):
        login_user(browser, link)
    with step('Go to profile page'):
        page = BasePage(browser, browser.current_url)
        page.go_to_profile_page()
    with step('Click "Edit" button'):
        page = ProfilePage(browser, browser.current_url)
        page.go_to_edit_page()

def remove_products_from_cart_and_fovorites(browser, link):
    with step('Go to cart page'):
        page = BasePage(browser, link)
        page.go_to_cart_page()
        sleep(3)
    with step('Remove all products from the cart'):
        page = CartPage(browser, browser.current_url)
        page.remove_products()
        sleep(3)
    with step('Go to favorites page'):
        page.go_to_favorites_page()        
        page = FavoritesPage(browser, browser.current_url)
        sleep(3)
    with step('Remove all products from the favorites'):
        page.remove_favorites_products()
        page.go_to_main_page()
        sleep(3)
    
    