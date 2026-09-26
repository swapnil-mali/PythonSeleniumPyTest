import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage

@pytest.mark.ui
@pytest.mark.login
def test_login_with_valid_creds(web_driver: WebDriver):
    login_page = LoginPage(web_driver)
    login_page.goto_login_page()
    assert login_page.wait_for_login_page_to_load(), "Failed to load login page"
    login_page.login()
    assert login_page.is_user_logged_in(), "Failed to login"