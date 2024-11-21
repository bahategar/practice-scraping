import re
from playwright.sync_api import sync_playwright, TimeoutError
from playwright.sync_api import Page, expect
import time

URL = "https://store.steampowered.com/specials"


if __name__ == '__main__':

    with sync_playwright() as p:
        # Define Browser object
        # browser = p.chromium.launch(headless=False)
        browser = p.firefox.launch(headless=False)
        # Define Page object
        page = browser.new_page()
        # Go to passed argument url
        page.goto(URL)

        # Wait the pages
        # Wait until the page has no more than 2 active network connections for at least 500 milliseconds.
        page.wait_for_load_state("networkidle")
        # Trigger any lazy-loading or additional content loading that the page might be doing. 
        #   This helps ensure that all parts of the page are loaded for scraping.
        page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
        # Wait until the initial HTML document has been completely loaded and parsed.
        page.wait_for_load_state("domcontentloaded")
        
        # Take Screenshot
        page.screenshot(path="example.png", full_page=True)

        # Close Browser
        browser.close()