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
        dropdown = self.browser.find_element(*BasePageLocators.SORT_DROPDOWN)
        script = "return arguments[0].offsetWidth === 0 && arguments[0].offsetHeight === 0;"
        if self.browser.execute_script(script, dropdown):
            return True
        else:
            return False
        
    '''element = driver.find_element_by_css_selector('selector')
    script = "return arguments[0].offsetWidth === 0 && arguments[0].offsetHeight === 0;"
    is_invisible = driver.execute_script(script, element)
    print("Элемент {}".format("невидим" if is_invisible else "видим"))
    '''
    
    # open page
    def open(self):
        self.browser.get(self.url)    

    # check that login link is present on the page
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"    
    