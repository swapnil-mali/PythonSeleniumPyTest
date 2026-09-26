import pytest
from core.driver.driver_factory import DriverFactory

@pytest.fixture
def web_driver(request):
    print("Test Setup")
    browser = request.config.getoption("--browser")
    driver_factory = DriverFactory(browser)
    driver = driver_factory.get_driver()
    driver.maximize_window()
    yield driver
    print("\nTest Teardown")
    driver.quit()

