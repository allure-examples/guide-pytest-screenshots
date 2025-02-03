import allure
from selenium.webdriver.common.by import By


@allure.title("Page should have a word in the title")
def test_main_page_title_should_have_word_in_title(selenium):
    with allure.step("Open the main page"):
        selenium.get("https://en.wikipedia.org/wiki/Software_testing")

    with allure.step("Look for a phrase in the title"):
        assert "Bad search" in selenium.title


@allure.title("Page should have a text entry element")
def test_main_page_should_have_text_entry(selenium):
    with allure.step("Open the main page"):
        selenium.get("https://en.wikipedia.org/wiki/Software_testing")
        attach_screenshot(selenium, "The main page.png")

    with allure.step("Find an element on the page"):
        elem = selenium.find_element(By.ID, "searchInput")
        attach_element_screenshot(elem, "The search input.png")
        assert elem is not None


def attach_screenshot(driver, name):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(
        screenshot,
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )


def attach_element_screenshot(element, name):
    allure.attach(
        element.screenshot_as_png,
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )
