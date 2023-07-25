import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--server_name", action="store", default="testhr")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    server_name = request.config.getoption("server_name")

    if browser_name == "chrome":
        service_obj = Service("/Users/daanswinnen/Documents/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(10)
        driver.maximize_window
    elif browser_name == "firefox":
        print("Firefox not supported")
    elif browser_name == "IE":
        print("IE not supported")

    if server_name == "testhr":
        driver.get("https://testhr.optimile.eu/")
    elif server_name == "test":
        driver.get("https://test.optimile.eu/")
    elif server_name == "plannertest":
        driver.get("https://plannertest.optimile.eu/tester/")

    request.cls.driver = driver
    yield
    driver.close

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = (
                    '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    path = r"/Users/daanswinnen/Documents/Screenshots/{}".format(name)
    driver.get_screenshot_as_file(path)