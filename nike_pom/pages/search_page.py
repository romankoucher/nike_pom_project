class SearchPage():
    def __init__(self, page):
        self.page = page

    def search_air(self):
        search_field = self.page.get_by_label("Enter Keyword or Item No.")
        search_field.fill("air")
        search_button = self.page.get_by_role("button", name="Submit search keywords")
        search_button.click()


    def verify_search_air_success(self):
        url = self.page.url
        assert url == "https://www.nike.ae/en/search?q=air&search-button=&lang=en_UG ", "URL is not as expected"


