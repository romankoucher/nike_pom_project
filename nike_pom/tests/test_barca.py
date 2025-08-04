class TestBarca():
    def test_barca(self, setup_nike):
        page, search_page, sale_page, barca_tshirt_page, jordan_search_page, men_shoes_page = setup_nike
        page.goto("https://www.nike.com/il/")
        barca_tshirt_page.barca_home_tshirt()