# test_login.py
import pytest
from playwright.sync_api import sync_playwright, expect
from login_page import LoginPage

def test_successful_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        # Assertion 1: URL changed to inventory page
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

        browser.close()

def test_invalid_login_shows_error():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.load()
        login_page.login("wrong_user", "wrong_pass")

        # Assertion 2: error message appears
        error_text = login_page.get_error_message()
        assert "Username and password do not match" in error_text

        browser.close()
