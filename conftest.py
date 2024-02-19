import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


#@pytest.fixture(params=["chrome", "firefox", "edge"])
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    #browser = request.param
    print(f"Creating driver for {browser}")
    if browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "remote-chrome":
        driver = webdriver.Remote('http://localhost:4444/wd/hub', options=webdriver.ChromeOptions())
    elif browser == "remote-firefox":
        driver = webdriver.Remote('http://localhost:4444/wd/hub', options=webdriver.FirefoxOptions())
    elif browser == "remote-edge":
        driver = webdriver.Remote('http://localhost:4444/wd/hub', options=webdriver.EdgeOptions())
    else:
        raise TypeError(f"Automation does not support browser {browser}")
    driver.implicitly_wait(10)
    yield driver
    print(f"Closing driver for {browser}")
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser for testing (edge or firefox)"
    )
