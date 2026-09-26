import config.config_reader as ConfReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocator

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def goto_base_page(self):
        self.driver.get(ConfReader.get_app_url())

    def is_base_root_enabled(self):
        base_title = self.driver.find_element(*BaseLocator.BASE_ROOT)
        return base_title.is_enabled()

    def wait_for_element_visible(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(BaseLocator.BASE_ROOT)
        )