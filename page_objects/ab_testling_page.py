from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class AbTestingPage(BasePage):
    __url = "https://the-internet.herokuapp.com/abtest"
    __ab_test_header = (By.TAG_NAME, "h3")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def current_url(self) -> str:
        return super()._driver.current_url

    def ab_landing_page_loaded_successfully(self):
        assert super().is_displayed(self.__ab_test_header), "The header is not displayed"
