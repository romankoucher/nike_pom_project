import os
import re
import time
from playwright.sync_api import Page, expect

class BarcaPage():

    def __init__(self, page: Page):
        self.page = page
        self.main_men_link = self.page.get_by_role("link", name="Men", exact=True)
        self.football_link = self.page.get_by_role('menuitem', name='Football').nth(2)
        self.barca_link = self.page.get_by_role("link", name="F.C. Barcelona F.C. Barcelona")
        self.sort_by = self.page.get_by_text("Sort By")
        self.lohi_button = self.page.get_by_label('Price: Low-High')


    def barca_home_tshirt(self):

        self.main_men_link.hover(timeout=60000)
        self.football_link.click(timeout=60000)
        expect(self.page).to_have_url("https://www.nike.com/il/football")
        self.barca_link.click(timeout=60000)
        expect(self.page).to_have_url("https://www.nike.com/il/w/fc-barcelona-5y174")
        self.sort_by.click(timeout=60000)
        self.lohi_button.click(timeout=60000)
        expect(self.page).to_have_url("https://www.nike.com/il/w/fc-barcelona-5y174?sortBy=priceAsc")













