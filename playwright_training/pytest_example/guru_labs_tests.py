
class TestGuruLabs():
    def test_flight_booking_flow(self, setup_playwright):
        page = setup_playwright
        page.goto("https://demo.guru99.com/test/newtours/index.php")
        page.locator("[name='userName']").fill("tutorial")
        page.locator("[name='password']").fill("tutorial")
        page.locator("[name='submit']").click()
        page.get_by_text('Flights').click()
        page.locator('[value="oneway"]').check()
        page.locator('[name = "passCount"]').select_option(value = '2')
        page.locator('[name = "fromPort"]').select_option(value='Frankfurt')
        page.locator('[name = "fromMonth"]').select_option(value='4')
        page.locator('[name = "fromDay"]').select_option(value='6')
        page.locator('[name = "toPort"]').select_option(value='London')
        page.locator('[name = "toMonth"]').select_option(value='5')
        page.locator('[name = "toDay"]').select_option(value='11')
        page.locator('[value = "First"]').check()
        page.locator('[name = "airline"]').select_option('Blue Skies Airlines')
        page.locator('[name = "findFlights"]').click()
        page.get_by_text('BACK TO HOME').click()
        page.wait_for_timeout(2000)
        print("There were no seats for your reservation ")






