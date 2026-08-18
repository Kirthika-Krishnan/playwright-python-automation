# base_page.py

class BasePage:
    def __init__(self, page):
        self.page = page  # the Playwright "page" (browser tab) gets passed in

    def navigate(self, url: str):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()
