class TestJordan():


    def test_jordan_search(self, setup_nike):
        page, search_page, sale_page, barca_tshirt_page, jordan_search_page, men_shoes_page = setup_nike
        page.goto("https://www.nike.com/il/")
        jordan_search_page.search_jordan()


