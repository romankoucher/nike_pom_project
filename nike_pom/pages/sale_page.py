from playwright.sync_api import expect


class SalePage():
    def __init__(self, page):
        self.page = page
        self.sale_main_menu_item = self.page.locator('span.b-megamenu__link-text.js-megamenu__link-text:has-text("Sale")')
        self.sale_for_men_link = self.page.locator('span.b-megasubmenu__link-text:has-text("Sale For Men")')

    def sale_for_men(self):
        self.sale_main_menu_item.hover()
        expect(self.sale_for_men_link).to_be_visible()
        self.sale_for_men_link.click()

    def verify_sale_male_success(self):
        expected_url_part = "https://www.nike.ae/en/sale/mens"
        expect(self.page).to_have_url(lambda url: url.startswith(expected_url_part))
