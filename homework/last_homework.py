from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.ebay.com/")
#     search_field = page.locator("[id = 'gh-ac' ]")
#     search_field.fill("table")
#     search_button = page.get_by_role('button', name="Search")
#     search_button.click()
#     page.wait_for_timeout(2000)
#     url = page.url
#     exp_url = "https://www.ebay.com/sch/i.html?_nkw=table&_sacat=0&_from=R40&_trksid=p4432023.m570.l1313"
#     if (url == exp_url):
#         print("you are at the right place")
#
#     page.close()
#     browser.close()
#     print("### Test end ###")


# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.ebay.com/")
#     search_field = page.locator("[id = 'gh-ac' ]")
#     search_field.fill("chair")
#     search_button = page.get_by_role("button", name="Search")
#     search_button.click()
#     page.wait_for_timeout(2000)
#     url = page.url
#     exp_url = "https://www.ebay.com/sch/i.html?_nkw=chair&_sacat=0&_from=R40&_trksid=m570.l1313"
#     if (url == exp_url):
#         print("you are at the right place")
#
#     page.close()
#     browser.close()
#     print("### Test end ###")

# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.ebay.com/")
#     search_field = page.locator("[id = 'gh-ac' ]")
#     search_field.fill("chair")
#     search_button = page.get_by_role("link", name="Advanced")
#     search_button.click()
#     page.wait_for_timeout(2000)
#     help_link = page.locator("#glbfooter").get_by_role("link", name="Help & Contact")
#     page.wait_for_timeout(2000)
#     help_link.click()
#     url = page.url
#     exp_url = "https://www.ebay.com/help/home"
#     if (url == exp_url):
#         print("you are at the right place")
#
#     page.close()
#     browser.close()
#     print("### Test end ###")


# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.calculator.net/")
#     grade_calc_link = page.get_by_role("link", name="Grade Calculator")
#     grade_calc_link.click()
#     page.wait_for_timeout(2000)
#     calculate_button = page.get_by_role("cell", name="Calculate Clear", exact=True).get_by_role("button", name="Calculate")
#     calculate_button.click()
#     page.wait_for_timeout(2000)
#     url = page.url
#     exp_url = "https://www.calculator.net/grade-calculator.html?d1=Homework+1&s1=90&l1=a&w1=5&d2=Project&s2=B&l2=b&w2=20&d3=Midterm+exam&s3=88&l3=b%2B&w3=20&d4=&s4=&l4=&w4=&d5=&s5=&l5=&w5=&d6=&s6=&l6=&w6=&d7=&s7=&l7=&w7=&d8=&s8=&l8=&w8=&sgoal=&lgoal=&wremain=&format=p&weight=p&plan=1&printit=0&ftype=1&x=Calculate"
#     if (url == exp_url):
#         print("you are at the right place")
#
#     page.close()
#     browser.close()
#     print("### Test end ###")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    customer_login = page.get_by_role("button", name="Customer Login")
    customer_login.click()

    url = page.url
    exp_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"
    if (url == exp_url):
        print("you are at the right place")

    page.close()
    browser.close()
    print("### Test end ###")
