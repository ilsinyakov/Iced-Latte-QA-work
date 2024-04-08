from .locators import BasePageLocators
from .pages.login_page import LoginPage
from .pages.profile_page import ProfilePage

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from allure import step


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # turn on implicitly wait

    # open page
    def open(self):
        self.browser.get(self.url)

    # check that the element is present on the page
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # check that login link is present on the page
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_profile_page(self):
        link = self.browser.find_element(*BasePageLocators.PROFILE_LINK)
        link.click()

class SetOfSteps:    
    def go_to_edit_profile_page(self, browser, link):
        with step('Open main page'):
            page = BasePage(browser, link)
            page.open()
        with step('Go to login page'):
            page.go_to_login_page()
        with step('Login existing user'):
            login_page = LoginPage(browser, browser.current_url)
            login_page.login_existing_user(email, password)
        with step('Go to profile page'):
            page = BasePage(browser, browser.current_url)
            page.go_to_profile_page()
        with step('Click "Edit" button'):
            page = ProfilePage(browser, browser.current_url)
            page.go_to_edit_page()
    