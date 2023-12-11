from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class elementalSeleniumPage(BasePage):
    __elemental_selenium_link = (By.LINK_TEXT, "Elemental Selenium")
    __header_tag = (By.TAG_NAME, "h1")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def click_selemental_link(self):
        super()._click(self.__elemental_selenium_link)

    def elemental_landing_page(self):
        super()._click(self.__elemental_selenium_link)
        super()._switch_tab("child")
        super()._wait_until_element_is_visible(self.__header_tag)
        assert super().is_displayed(self.__header_tag)

        print("Page title for browser tab:")
        print(self._driver.title)
        page_url = self._driver.current_url
        print("MADE IT")
        print(page_url)
        assert page_url == "https://elementalselenium.com/", "The url is incorrect for elemental selenium"