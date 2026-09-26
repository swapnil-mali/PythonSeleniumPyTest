import config.config_reader as ConfReader
from locators.login_locators import LoginLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def goto_login_page(self):
        self.driver.get(ConfReader.get_app_url())

    def wait_for_login_page_to_load(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(LoginLocator.SUBMIT_BUTTON)
        )

    def login(self):
        username_input = self.driver.find_element(*LoginLocator.USERNAME_INPUT)
        username_input.send_keys(ConfReader.get_username())
        password_input = self.driver.find_element(*LoginLocator.PASSWORD_INPUT)
        password_input.send_keys(ConfReader.get_user_password())
        submit_btn = self.driver.find_element(*LoginLocator.SUBMIT_BUTTON)
        submit_btn.click()

    def is_user_logged_in(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(LoginLocator.INVENTORY_ITEM)
        )