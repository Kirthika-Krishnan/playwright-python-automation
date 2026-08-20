from playwright.sync_api import expect
from login_page import LoginPage

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_invalid_login_shows_error(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("wrong_user", "wrong_pass")
    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text