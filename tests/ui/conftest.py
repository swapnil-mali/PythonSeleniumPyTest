import pytest
from core.driver.driver_factory import GetDriver

@pytest.fixture
def webdriver(request):
    print("Test Setup")
    browser = request.config.getoption("--browser")
    driver = GetDriver(browser).get_driver()
    yield driver
    print("\nTest Teardown")
    driver.quit()

