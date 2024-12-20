import pytest
from selenium.webdriver import Chrome, ChromeOptions

@pytest.fixture(scope="session")
def driver():
    # setup
    options = ChromeOptions()
    options.add_argument("--incognito")
    # options.add_argument("--headless")
    driver = Chrome(options=options)
    # driver = SetupDriver()
    driver.maximize_window()
    yield driver
    # teardown
    driver.quit()