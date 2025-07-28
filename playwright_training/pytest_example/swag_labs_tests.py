class TestSwaglabs():
    # def - saved word for function
    # test - mandatory
    # def test_login_correct_user(self, setup_playwright):
    #     page = setup_playwright
    #     page.goto("https://www.saucedemo.com/")
    #     print("Trying to login with correct parameters ")
    #     user = page.locator("[id='user-name']")
    #     password = page.locator("[id='password']")
    #     login_button = page.get_by_text("Login")
    #     user.fill("standard_user")
    #     password.fill("secret_sauce")
    #     login_button.click()
    #     assert page.url == "https://www.saucedemo.com/inventory.html","URL is not as expected"
    #
    #  def test_login_incorrect_user(self, setup_playwright):
    #      page = setup_playwright
    #      page.goto("https://www.saucedemo.com/")
    #      print("Trying to login with incorrect parameters ")
    #      user = page.locator("[id='user-name']")
    #      password = page.locator("[id='password']")
    #      login_button = page.get_by_text("Login")
    #      user.fill("fake_user")
    #      password.fill("fake_password")
    #      login_button.click()
    #      assert page.url == "https://www.saucedemo.com/inventory.html"
    #
    # def test_get_price_first(self, setup_playwright):
    #     page = setup_playwright
    #     page.goto("https://www.saucedemo.com/")
    #     print("Trying to login with correct parameters ")
    #     user = page.locator("[id='user-name']")
    #     password = page.locator("[id='password']")
    #     login_button = page.get_by_text("Login")
    #     user.fill("standard_user")
    #     password.fill("secret_sauce")
    #     login_button.click()
    #     prices = page.query_selector_all("[class='inventory_item_price']")# It brings all elements of class 'inventory_item_price'
    #     for price in prices:
    #         print(price.text_content()) # это текст цены
    #     print("after query selector all")
    #     for price in prices:
    #         item_price = float(price.text_content().replace("$", "")) # price.text_content() - текст цены, .replace("$", "") - убирает $ и переводим в число
    #         assert item_price < 100, f"Price {item_price} more than $100"
    #     print("All items cost less than $100")

    def test_login_by_css(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        user = page.locator("input[id = 'user-name']")
        password = page.locator("input[data-test = 'password']")
        login_button = page.locator("input[class = 'submit-button btn_action']")
        user.fill("abc")
        password.fill("fake")
        login_button.click()
        print("debug point")

    # def test_get_price_first(self, setup_playwright):
    #     page = setup_playwright
    #     page.goto("https://www.saucedemo.com/")
    #     print("Trying to login with correct parameters ")
    #     user = page.locator("[id='user-name']")
    #     password = page.locator("[id='password']")
    #     login_button = page.get_by_text("Login")
    #     user.fill("standard_user")
    #     password.fill("secret_sauce")
    #     login_button.click()
    #     page.get_by_role("combobox").select_option("hilo")
    #     print("Sorting changed using ARIA roles")
    #     first_price_text = page.locator(".inventory_item_price").first.text_content()
    #     first_price = float(first_price_text.replace("$", ""))
    #     assert first_price <= 100, f"The most expensive item is: ${first_price}"

    # def test_get_price_first(self, setup_playwright):
    #     page = setup_playwright
    #     page.goto("https://www.demoblaze.com/")
    #     contact_link = page.get_by_role('link', name='Contact').click()
    #     page.wait_for_timeout(1000)
    #     close_button = page.get_by_role('button', name='Close')
    #     assert page.url == "https://www.demoblaze.com/", "you didn't press the 'Close' button"
