from selenium import webdriver
import core.driver.browser_options as Options

class DriverFactory:
    def __init__(self, browser = 'chrome'):
        self.browser = browser.lower()

    def get_driver(self):
        if self.browser == 'chrome':
            return self._get_chrome_driver()
        elif self.browser == 'firefox':
            return self._get_firefox_driver()
        else:
            raise ValueError(f"Browser type - {self.browser} not supported")

    def _get_chrome_driver(self):
        return webdriver.Chrome(options=Options.get_chrome_options())

    def _get_firefox_driver(self):
        return webdriver.Firefox()

    def load_application():
        pass

