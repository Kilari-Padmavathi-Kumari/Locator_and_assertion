'''
import time
def test_popup(page):
    page.goto("https://the-internet.herokuapp.com/windows")

    with page.expect_popup() as popup_info:
        page.get_by_text("Click Here").click()

    popup = popup_info.value

    popup.wait_for_load_state()

    print("Popup URL:", popup.url)
    print("Popup Title:", popup.title())

    time.sleep(2)'''


def test_popup(page):
    page.goto("https://the-internet.herokuapp.com/windows")

    # See the first window
    page.wait_for_timeout(3000)

    with page.expect_popup() as popup_info:
        page.get_by_text("Click Here").click()

    popup = popup_info.value

    # See the second window
    popup.wait_for_load_state()
    popup.wait_for_timeout(3000)

    print("First Window URL:", page.url)
    print("Second Window URL:", popup.url)

    # Keep second window visible for 5 seconds
    popup.wait_for_timeout(5000)