from .locators import BasePageLocators

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # turn on implicitly wait

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_profile_page(self):
        link = self.browser.find_element(*BasePageLocators.PROFILE_LINK)
        link.click()    

    # check that the element is present on the page
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    # check that sort drop-down is not present on the page
    def is_dropdown_not_present(self):
        try:
            dropdown = self.browser.find_element(*BasePageLocators.SORT_DROPDOWN)
            return False
        except:
            return True
    
    # open page
    def open(self):
        self.browser.get(self.url)    

    # check that login link is present on the page
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"    
    