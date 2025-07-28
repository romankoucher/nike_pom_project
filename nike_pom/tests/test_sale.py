class TestSale():
    def test_sale(self, setup_nike):
        page, search_page, sale_page = setup_nike
        sale_page.sale_for_men()
