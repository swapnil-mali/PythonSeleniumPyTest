import time
from selenium.webdriver.common.by import By

def test_base_page_loads(webdriver):
    webdriver.get("https://www.saucedemo.com/")
    webdriver.maximize_window()
    time.sleep(1)
    element = webdriver.find_element(By.ID, "user-name")
    assert element.is_enabled(), "Element is not enabled"
    time.sleep(2)
