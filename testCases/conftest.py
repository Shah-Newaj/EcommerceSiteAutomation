import pytest
from selenium import webdriver

@pytest.fixture()
def browserInstance():
    driver = webdriver.Chrome()
    # Global Time out - max 5 seconds
    driver.implicitly_wait(5)  # Applying Implicit Wait
    return driver   # yield can also be used instead of return