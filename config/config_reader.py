import os

def get_app_url():
    return "https://www.saucedemo.com/"

def get_user_password():
    try:
        return os.environ["TEST_PASSWORD"]
    except KeyError:
        raise ValueError("TEST Password is not set in the environment")

def get_username():
    return "standard_user"