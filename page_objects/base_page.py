from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open_url(self, url: str):
        self._driver.get(url)

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str):
        self._wait_until_element_is_visible(locator)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 2):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _wait_until_url_contains(self, url: str, time: int = 1):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.url_contains(url))

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 2):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_is_not_visible(self, locator: tuple, time: int = 1):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.invisibility_of_element_located(locator))

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _contains_text(self, locator: tuple, text: str):
        assert locator.text.__contains__(str)

    def _switch_tab(self, tab: str):
        match tab:
            case "child":
                window = self._driver.window_handles[1]
                print('Switching to child')
            case "parent":
                window = self._driver.window_handles[0]
            case "original":
                window = self._driver.current_window_handle
            case _:
                "missing window"
        self._driver.switch_to.window(window)
