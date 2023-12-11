from pydoc import text

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestAddRemoveElements:

    @pytest.mark.regression
    def test_add_remove_elements(self, driver):
        wait = WebDriverWait(driver, 5)
        # Go to webpage
        driver.get("https://the-internet.herokuapp.com/")
        assert wait.until(ec.invisibility_of_element_located((By.XPATH, "//a[contains(., 'Welcome to the-internet')]")),
                          "Should be out of the main page")

        allure.attach(driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

        # Click on Add Remove Testing
        ab_testing_link = driver.find_element(By.XPATH, "//a[contains(., 'Add/Remove Elements')]")
        ab_testing_link.click()
        assert wait.until(ec.invisibility_of_element_located((By.XPATH, "//a[contains(., 'Welcome to the-internet')]")),
                          "Should be out of the main page")

        # Verify page is on Add Remove Testing
        header_text = driver.find_element(By.TAG_NAME, "h3")
        assert header_text.is_displayed()
        assert header_text.text == 'Add/Remove Elements'
        assert wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Elemental Selenium")))

        # Click Elemental Selenium
        elemental_selenium_link = driver.find_element(By.LINK_TEXT, "Elemental Selenium")
        elemental_selenium_link.click()

        # Confirm page landed on Elemental Selenium

        # obtain window handle of browser in focus
        p = driver.current_window_handle

        # obtain parent window handle
        parent = driver.window_handles[0]

        # obtain browser tab window
        child = driver.window_handles[1]

        # switch to browser tab
        driver.switch_to.window(child)

        print("Page title for browser tab:")
        print(driver.title)
        page_url = driver.current_url
        print(page_url)
        assert page_url == "https://elementalselenium.com/"

        header_text = driver.find_element(By.TAG_NAME, "h1")
        assert header_text.is_displayed()
