from pages.home_page import HomePage


class HomeFlow:

    def __init__(self, page):
        self.page = page
        self.home_page = HomePage(page)

    def open_home_page(self):
        self.home_page.open()

    def check_home_loaded(self):
        return self.home_page.is_logo_visible()