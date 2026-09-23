from tkinter import dialog

from playwright.sync_api import Page, expect

def test_UIChecks(page:Page):
    #hide/display and placeholder check
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #alertBoxes
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(2)

   
    