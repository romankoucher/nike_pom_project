class TestSale():
    def test_sale(self, setup_nike):
        page, search_page, sale_page, barca_tshirt_page, jordan_search_page, men_shoes_page= setup_nike
        page.goto("https://www.nike.ae/en/home/")
        sale_page.sale_for_men()
