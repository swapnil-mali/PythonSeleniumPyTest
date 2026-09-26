import pytest
from pages.base_page import BasePage

@pytest.mark.ui
@pytest.mark.smoke
def test_base_page_loads(web_driver):
    base_page = BasePage(web_driver)
    base_page.goto_base_page()
    assert base_page.wait_for_element_visible(), "Failed to load base page"
    assert base_page.is_base_root_enabled(), "Element is not enabled"
