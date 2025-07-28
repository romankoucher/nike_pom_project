import time

from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.calculator.net/")
    bmi_button = page.get_by_text("BMI Calculator")
    bmi_button.click()
    exp_url = "https://www.calculator.net/bmi-calculator.html"
    time.sleep(3)
    url = page.url
    if (url == exp_url):
        print(" Link button works as expected")
    else:
        print("url is not found")
    fitness_button = page.locator("//*[contains(text(), 'FITNESS')]")
    fitness_button.click()

    page.close()
    browser.close()
    print("### Test end ###")
