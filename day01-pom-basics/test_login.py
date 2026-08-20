from playwright.sync_api import expect
from login_page import LoginPage
from config import TEST_USERNAME, TEST_PASSWORD

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(TEST_USERNAME, TEST_PASSWORD)
    expect(page).to_have_url(f"{login_page.URL}/inventory.html")

def test_invalid_login_shows_error(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("wrong_user", "wrong_pass")   # intentionally still hardcoded — this is testing a FAILURE case
    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text