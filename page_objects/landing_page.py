from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LandingPage(BasePage):
    __url = "https://the-internet.herokuapp.com/"
    __url_ab_page = "abtest"
    __ab_testing_link = (By.XPATH, "//a[contains(., 'A/B Testing')]")
    __add_remove_link = (By.XPATH, "//a[contains(., 'Add/Remove Elements')]")
    __home_page_header = (By.XPATH, "//a[contains(., 'Welcome to the-internet')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def click_ab_testing_link(self):
        super()._click(self.__ab_testing_link)
        super()._wait_until_url_contains(self.__url_ab_page)

    def click_add_remove_link(self):
        super()._click(self.__ab_testing_link)
        super()._wait_until_element_is_not_visible(self.__home_page_header)
