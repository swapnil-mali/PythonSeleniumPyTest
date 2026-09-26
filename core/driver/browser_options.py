from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def get_chrome_options():
    options = ChromeOptions()
    # disble chrome level logs
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # set logging level to off
    options.add_argument("--log-level=3")
    return options