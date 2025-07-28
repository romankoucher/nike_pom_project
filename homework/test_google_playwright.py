from playwright.sync_api import sync_playwright #Импортируем синхронный API Playwright

def test_google_title(): # Создаём тестовую функцию для pytest (начинается со test_)
    with sync_playwright() as p: # Запускаем движок Playwright (как "менеджер контекста")
        browser = p.chromium.launch(headless=True)  # Открываем браузер без интерфейса
        page = browser.new_page()                   # Открываем новую вкладку браузера
        page.goto("https://www.google.com")         # Переходим на сайт Google
        assert "Google" in page.title()             # Проверяем, что заголовок страницы содержит слово "Google"
        browser.close()                             # Закрываем браузер





