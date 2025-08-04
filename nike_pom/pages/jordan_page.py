class JordanPage():
    def __init__(self, page):
        self.page = page

    def search_jordan(self):
        search_button = self.page.get_by_role("button", name="Search")
        search_button.click()
        search_field = self.page.get_by_placeholder("Search")
        search_field.fill("jordan")
        self.page.keyboard.press("Enter")
        search_gender = self.page.get_by_role("button", name="Gender", exact=True)
        search_gender.click()
        unisex_box = self.page.get_by_text("Unisex").filter(has_text="Unisex").first
        unisex_box.wait_for(state="visible", timeout=10000)
        unisex_box.click()

    def verify_search_air_success(self):
        url = self.page.url
        assert url == "https://www.nike.com/il/w/unisex-3rauv?q=jordan ", "URL is not as expected"