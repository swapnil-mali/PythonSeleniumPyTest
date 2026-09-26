from selenium.webdriver.common.by import By

class LoginLocator:
    LOGIN_LOGO = (By.XPATH, "//div[@class='login_logo']")
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    SUBMIT_BUTTON = (By.ID, "login-button")
    INVENTORY_ITEM = (By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']")