# men_shoes_page.py
from playwright.sync_api import expect, Page


class MenShoesPage():

    def __init__(self, page: Page):
        self.page = page
        self.main_men_link = self.page.get_by_role("link", name="Men", exact=True)
        self.all_shoes_link = self.page.get_by_role("menuitem", name="All Shoes")
        self.search_by_price = self.page.get_by_role("button", name="Shop By Price", exact=True)
        self.by_price_box = self.page.get_by_text("Under ₪ 259.9").filter(has_text="Under ₪ 259.9").first
        self.shoes_sort_by = self.page.get_by_text("Sort By")
        self.lohi_button = self.page.get_by_label('Price: Low-High')

    def men_shoes_sort(self):
        self.main_men_link.hover(timeout=10000)
        self.all_shoes_link.click(timeout=10000)
        expect(self.page).to_have_url("https://www.nike.com/il/w/mens-shoes-nik1zy7ok")
        self.search_by_price.click()
        self.by_price_box.wait_for(state="visible", timeout=10000)
        self.by_price_box.click(timeout=10000)
        self.shoes_sort_by.click(timeout=60000)
        self.lohi_button.click(timeout=60000)
        expect(self.page).to_have_url("https://www.nike.com/il/w/mens-under-2599-shoes-6xw70znik1zy7ok?sortBy=priceAsc")

    def verify_search_men_shoes(self):
        url = self.page.url
        assert url == "https://www.nike.com/il/w/mens-under-2599-shoes-6xw70znik1zy7ok?sortBy=priceAsc", "URL is not as expected"
