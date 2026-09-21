#import time

from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto("https://qa.rams.emergobyul.com/login")
    page.get_by_label("Email").fill("padmavathi.kilari@fissionlabs.com")
    page.get_by_label("Password").fill("sjkashdasxb")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_text("Error")).to_be_visible()
    expect(page.get_by_text("Invalid email and/or password.")).to_be_visible()

  #  time.sleep(5)