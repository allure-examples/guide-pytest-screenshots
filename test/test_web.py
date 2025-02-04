import allure
from playwright.sync_api import expect


@allure.title("Page should have a word in the title")
def test_main_page_title_should_have_word_in_title(page):
    with allure.step("Open the main page"):
        page.goto("https://en.wikipedia.org/wiki/Software_testing")

    with allure.step("Look for a phrase in the title"):
        expect(page).to_have_title("Not the actual title")


@allure.title("Page should have a text entry element")
def test_main_page_should_have_text_entry(page):
    with allure.step("Open the main page"):
        page.goto("https://en.wikipedia.org/wiki/Software_testing")
        attach_screenshot(page, "The loaded page.png")

    with allure.step("Find an element on the page"):
        elem = page.get_by_role("search")
        attach_element_screenshot(elem, "The search input.png")
        expect(elem).to_be_visible()


def attach_screenshot(page, name):
    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )


def attach_element_screenshot(element, name):
    allure.attach(
        element.screenshot(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )
