import csv
from playwright.sync_api import Playwright, sync_playwright

def scrape_google_job() -> None:
    with sync_playwright() as playwright:
        # Seleccionamos el navegador "chromium"
        browser = playwright.chromium.launch(headless=False)

        try:
            # Creamos un contexto y abrimos una nueva página
            context = browser.new_context()
            page = context.new_page()

            page.goto('https://www.google.com/search?q=data+scientist+trabajos')

            page.wait_for_selector('"y más de 100 empleos más"').click()
            page.wait_for_selector('"300 km"').click()

            books = []
            for item in page.query_selector_all('.oNwCmf'):
                book = {}
                #item.click()

                name_el = item.query_selector('.vNEEBe')
                book['name'] = name_el.inner_text()

                price_el = item.query_selector('.Qk80Jf')
                book['price'] = price_el.inner_text()

                books.append(book)

            print(books)

            div_cd_xzfe = page.query_selector('div.YgLbBe.YRi0le')
            a = div_cd_xzfe.inner_text()
            print(a)

            page.screenshot(path="example.png")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        finally:
            # Cerramos el navegador
            browser.close()

scrape_google_job()
