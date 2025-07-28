from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ebay.com/")
    search_menu = page.locator("[id='gh-ac']")
    search_button = page.locator("[id ='gh-search-btn']")
    search_menu.click()
    search_menu.fill("Shoes")
    search_button.click()

    page.close()
    browser.close()
    print("### Test end ###")
