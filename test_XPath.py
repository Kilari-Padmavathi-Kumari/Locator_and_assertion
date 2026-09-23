from playwright.sync_api import Page

import time

def test_login(page: Page):

    page.goto("https://www.saucedemo.com/")

    page.locator("//input[@id='user-name']").fill("standard_user")

    page.locator("//input[@id='password']").fill("secret_sauce")

    page.locator("//input[@id='login-button']").click()

    time.sleep(2)