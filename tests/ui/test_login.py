import pytest


class TestLogin:

    def test_login_page_loads(self, page):
        """Verify login page loads successfully"""
        assert page.title() != ""

    def test_login_page_has_username_field(self, page):
        """Verify username input field is visible"""
        username_field = page.locator("input[type='email'], input[name='username']")
        assert username_field.is_visible()

    def test_login_page_has_password_field(self, page):
        """Verify password input field is visible"""
        password_field = page.locator("input[type='password']")
        assert password_field.is_visible()

    def test_login_page_has_submit_button(self, page):
        """Verify login/submit button is visible"""
        submit_button = page.locator("button[type='submit']")
        assert submit_button.is_visible()

    def test_invalid_login_shows_error(self, page):
        """Verify error message appears on invalid credentials"""
        page.locator("input[type='email'], input[name='username']").fill("invalid@test.com")
        page.locator("input[type='password']").fill("wrongpassword")
        page.locator("button[type='submit']").click()
        error = page.locator(".error, [role='alert']")
        assert error.is_visible()
