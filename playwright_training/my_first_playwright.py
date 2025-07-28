from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user = page.locator("[id='user-name']")
    password = page.locator("[id='password']")
    login_button = page.get_by_text("Login")
    login_button_by_name = page.locator("[name='login-button']")  # example for name
    user.click()
    user.fill("standard_user")
    password.fill("secret_sauce")
    login_button.click()
    url = page.url
    expected_url = 'https://www.saucedemo.com/inventory.html'
    if(url == expected_url):
        print('Login is successful')

    page.close()
    browser.close()
    print("### Test end ###")
