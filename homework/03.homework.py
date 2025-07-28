# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.ebay.com/")
#     advanced_button = page.get_by_text("advanced")
#     advanced_button.click()
#     url = page.url
#     exp_url = "https://www.ebay.com/sch/ebayadvsearch"
#     if (url == exp_url):
#         print("you are at the right place")
#
#     page.close()
#     browser.close()
#     print("### Test end ###")
import time

# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://demo.guru99.com/test/newtours/index.php")
#     enter_username = page.locator('input[name="userName"]')
#     enter_username.fill('tutorial')
#     enter_pass = page.locator('input[name="password"]')
#     enter_pass.fill('tutorial')
#     submit_button = page.get_by_role('button', name='Submit')
#     submit_button.click()
#     page.wait_for_url("**/login_sucess.php")
#     url = page.url
#     exp_url = "https://demo.guru99.com/test/newtours/login_sucess.php"
#     if (url == exp_url):
#         print("you are at the right place")
#
#     page.close()
#     browser.close()
#     print("### Test end ###")

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.zara.com/il/en/")
    help_button = page.get_by_role('link',name='HELP').click()
    time.sleep(10)
    url = page.url
    exp_url = "https://www.zara.com/il/en/help-center"
    if (url == exp_url):
        print("you are at the right place")

    page.close()
    browser.close()
    print("### Test end ###")
