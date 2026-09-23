import playwright
from playwright.sync_api import expect


def test_firefox_omada(playwright: playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://app.omada-staging.io/",
        wait_until="networkidle"
    )

    # Email
    page.get_by_placeholder("Enter your email").fill(
        "testomada02@gmail.com"
    )

    # Password
    page.get_by_placeholder("Enter password").fill(
        "Omada@#02"
    )

    page.get_by_role("button", name="Sign In").click()

    expect(
        page.get_by_text("Incorrect username or password.")
    ).to_be_visible()

    expect(
        page.get_by_text("Please try again")
    ).to_be_visible()

    expect(
        page.get_by_text("English")
    ).to_be_visible()

    browser.close()
'''



import playwright
from playwright.sync_api import expect


def test_firefox_omada(playwright: playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://app.omada-staging.io/",
        wait_until="networkidle"
    )

    page.locator('input[type="email"]').fill(
        "testomada02@gmail.com"
    )

    page.locator('input[type="password"]').fill(
        "Omada@#02"
    )

    page.get_by_role("button", name="Sign In").click()

    expect(
        page.get_by_text("Incorrect username or password.")
    ).to_be_visible()

    expect(
        page.get_by_text("Please try again")
    ).to_be_visible()

    expect(
        page.get_by_text("English")
    ).to_be_visible()

    browser.close()

    '''