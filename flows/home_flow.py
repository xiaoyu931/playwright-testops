from pages.home_page import HomePage
from core.flow_result import FlowResult

class HomeFlow:

    def __init__(self, page):
        self.page = page
        self.home_page = HomePage(page)

    def open_home_page(self):
        self.home_page.open()

    def check_home_loaded(self):
        visible = self.home_page.is_logo_visible()

        if visible:
            return FlowResult(True, "首页加载成功")
        else:
            return FlowResult(False, "首页加载失败：Logo 未出现")