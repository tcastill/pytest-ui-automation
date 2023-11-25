import time

import pytest
from selenium.webdriver.common.by import By


class TestAddRemoveElements:

    @pytest.mark.regression
    def test_add_remove_elements(self, driver):
        # Go to webpage
        driver.get("https://the-internet.herokuapp.com/")

        # Click on Add Remove Testing
        ab_testing_link = driver.find_element(By.XPATH, "//a[contains(., 'Add/Remove Elements')]")
        ab_testing_link.click()
        time.sleep(1)

        # Verify page is on Add Remove Testing
        header_text = driver.find_element(By.TAG_NAME, "h3")
        assert header_text.is_displayed()
        assert header_text.text == 'Add/Remove Elements'

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
        assert page_url == "https://elementalselenium.com/"

        header_text = driver.find_element(By.TAG_NAME, "h1")
        assert header_text.is_displayed()
