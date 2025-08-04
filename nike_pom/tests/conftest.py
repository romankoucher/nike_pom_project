import pytest
from playwright.sync_api import sync_playwright, expect

from nike_pom.pages.barca_tshirt_page import BarcaPage
from nike_pom.pages.men_shoes_page import MenShoesPage
from nike_pom.pages.sale_page import SalePage
from nike_pom.pages.search_page import SearchPage
from nike_pom.pages.jordan_page import JordanPage

expect.set_options(timeout=10_000)


@pytest.fixture()
def setup_nike():
    print("### Test start ###")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        search_page = SearchPage(page)
        sale_page = SalePage(page)
        barca_tshirt_page = BarcaPage(page)
        jordan_search_page = JordanPage(page)
        men_shoes_page = MenShoesPage(page)



        yield page, search_page, sale_page, barca_tshirt_page,jordan_search_page, men_shoes_page
        page.wait_for_timeout(10000)
        print("### Test end ###")
        # page.close()
        # browser.close()