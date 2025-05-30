import pytest
from selenium import webdriver

def pytest_addoption(parser):   #This will get the value from CLI/hooks
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

# setup and teardown in one function. Separated with yield step.
@pytest.fixture()
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser ..............")
    elif browser_name == "edge":
        driver = webdriver.Edge()
        print("Launching Microsoft Edge browser ..............")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome browser ..............")

    # Global Time out - max 5 seconds
    driver.implicitly_wait(5)  # Applying Implicit Wait
    yield driver   # before test function execution
    driver.close()  # post test function execution