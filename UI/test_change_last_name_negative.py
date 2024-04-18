from .pages.base_page import BasePage
from .pages.profile_page import ProfilePage
from .pages.edit_profile_page import EditProfilePage
from .set_of_steps import go_to_edit_profile_page
from .configs import link, new_last_name_negative

from allure import step, title, severity, story, severity_level
import pytest


@title("Test Change Last Name Negative")
@story("Personal Account")
# @allure.description("")
# @allure.tag("")
@severity(severity_level.NORMAL)
@pytest.mark.parametrize('new_last_name', new_last_name_negative)
def test_user_cant_change_last_name(browser, new_last_name):
    with step('Go to Edit Profile Page'):        
        go_to_edit_profile_page(browser, link)
    with step('Enter new Negative Last Name'):
        page = EditProfilePage(browser, browser.current_url)
        page.change_last_name(new_last_name)
    with step('Click "Save Changes" button'):
        page.save_change()    
    with step('Assert Error message is present'):                
        assert page.is_error_message_present(('Invalid Last name format. Use extended Latin letters', 
                                              'Last name is required', 
                                              'Server Error: Internal server error')
                                             ), 'Error message is not present'
    with step('Go to Main Page'):        
        page.go_to_main_page()
    with step('Go to Profile Page'):
        page = BasePage(browser, browser.current_url)
        page.go_to_profile_page()        
    with step('Assert New Negative Last Name is not present in profile'):
        page = ProfilePage(browser, browser.current_url)
        assert page.is_not_negative_last_name_present(new_last_name), 'New Negative Last Name is present in profile'
        