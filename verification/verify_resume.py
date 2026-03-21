from playwright.sync_api import Page, expect, sync_playwright
import re

def test_resume_content(page: Page):
    # Navigate to the site
    page.goto("http://localhost:8000")

    # Click on the Resume nav link
    page.click("button.navbar-link:has-text('Resume')")

    # Wait for the resume article to be active
    resume_article = page.locator("article.resume")
    expect(resume_article).to_have_class(re.compile(r"active"))

    # Take a screenshot
    page.screenshot(path="verification/final_resume_verification.png", full_page=True)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_resume_content(page)
        finally:
            browser.close()
