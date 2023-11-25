import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@pytest.mark.links
@pytest.mark.parametrize("base_url,expected_error", [("https://the-internet.herokuapp.com/",
                                                      "The header is not displayed")])
class TestAbPage:

    def test_login_to_ab_link(self, driver, base_url, expected_error):
        # Go to webpage
        driver.get(base_url)

        # Click on A/B Testing
        ab_testing_link = driver.find_element(By.XPATH, "//a[contains(., 'A/B Testing')]")
        ab_testing_link.click()
        time.sleep(1)

        # Verify page is on A/B Testing
        header_text = driver.find_element(By.TAG_NAME, "h3")
        assert header_text.is_displayed(), expected_error
        assert header_text.text.__contains__('A/B Test'), "The header is missing A/B text on this page"

        # Click Elemental Selenium
        elemental_selenium_link = driver.find_element(By.LINK_TEXT, "Elemental Selenium")
        elemental_selenium_link.click()
        time.sleep(5)

        # Confirm page landed on Elemental Selenium

        # obtain window handle of browser in focus
        p = driver.current_window_handle

        # obtain parent window handle
        parent = driver.window_handles[0]

        # obtain browser tab window
        chld = driver.window_handles[1]

        # switch to browser tab
        driver.switch_to.window(chld)

        print("Page title for browser tab:")
        print(driver.title)
        page_url = driver.current_url
        print(page_url)
        assert page_url == "https://elementalselenium.com/", "The url is incorrect for elemental selenium"

        header_text = driver.find_element(By.TAG_NAME, "h1")
        assert header_text.is_displayed()
        assert header_text.text == 'Make sure your code lands'

    def test_multiple_login_to_ab_link(self, driver, base_url, expected_error):
        # Go to webpage
        driver.get(base_url)

        for x in range(6):
            ab_testing_link = driver.find_element(By.XPATH, "//a[contains(., 'A/B Testing')]")
            ab_testing_link.click()
            time.sleep(1)

            # Verify page is on A/B Testing
            header_text = driver.find_element(By.TAG_NAME, "h3")
            assert header_text.is_displayed(), expected_error
            assert header_text.text.__contains__('A/B Test'), "The header is missing A/B text on this page"

            # Click back
            driver.back()
            time.sleep(1)
