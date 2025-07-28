import pytest
from playwright.sync_api import sync_playwright, expect

from nike_pom.pages.sale_page import SalePage
from nike_pom.pages.search_page import SearchPage

expect.set_options(timeout=10_000)


@pytest.fixture()
def setup_nike():
    print("### Test start ###")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.nike.ae/en/home/")

        search_page = SearchPage(page)
        sale_page = SalePage(page)



        yield page, search_page, sale_page
        page.wait_for_timeout(10000)
        print("### Test end ###")
        page.close()
        browser.close()