from playwright.sync_api import sync_playwright


def extract_full_body_html(from_url : str, wait_for : str =None) -> str:
    with sync_playwright() as p:
        # Define Browser object
        # browser = p.chromium.launch(headless=False)
        browser = p.firefox.launch()
        # Define Page object
        page = browser.new_page()
        # Go to passed argument url
        page.goto(from_url)

        # Wait the pages
        # Wait until the page has no more than 2 active network connections for at least 500 milliseconds.
        page.wait_for_load_state("networkidle")
        # Trigger any lazy-loading or additional content loading that the page might be doing. 
        #   This helps ensure that all parts of the page are loaded for scraping.
        page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
        # Wait until the initial HTML document has been completely loaded and parsed.
        page.wait_for_load_state("domcontentloaded")
        if wait_for:
            # Wait until specific selector appears
            page.wait_for_selector(wait_for)

        # Parsing HTML
        html = page.inner_html('body')

        # Close the browser
        browser.close()

        return html