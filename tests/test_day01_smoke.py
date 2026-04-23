# def test_open_testops_home(page):
#     page.goto("http://localhost:3000")
#     page.wait_for_load_state("networkidle")
#
#     # assert page.locator("text=TestOps").is_visible()
#     assert page.get_by_text("TestOps").is_visible()


# from pages.home_page import HomePage
#
#
# def test_open_testops_home(page):
#     page.goto("http://localhost:3000")
#
#     home = HomePage(page)
#
#     assert home.is_logo_visible()


from flows.home_flow import HomeFlow


def test_open_testops_home(page):
    flow = HomeFlow(page)

    flow.open_home_page()
    result = flow.check_home_loaded()

    assert result.success, result.message