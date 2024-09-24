import os
import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from utilities.Settings import (
    cache_directory,
    chromedriver_directory,
    geckodriver_directory,
    screenshot_directory,
)

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--server_name", action="store", default="staging")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    server_name = request.config.getoption("server_name")

    if os.path.exists(cache_directory):
        pass
    else:
        os.mkdir(cache_directory)

    if browser_name == "chrome":
        service_obj = Service(chromedriver_directory)
        options = Options()
        options.add_argument("--remote-allow-origins=*")
        options.add_argument("--disable-search-engine-choice-screen")
        options.add_experimental_option(
            "prefs", {"download.default_directory": cache_directory}
        )
        driver = webdriver.Chrome(service=service_obj, options=options)
        driver.implicitly_wait(10)
        driver.maximize_window()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()

    elif browser_name == "edge":
        driver = webdriver.Edge()
        driver.implicitly_wait(10)
        driver.maximize_window()

    if server_name == "testhr":
        driver.get("https://testhr.optimile.eu/")
    elif server_name == "test":
        driver.get("https://test.optimile.eu/")
    elif server_name == "plannertest":
        driver.get("https://plannertest.optimile.eu/tester/")
    elif server_name == "qatest":
        driver.get("https://qatest.optimile.eu/welcome/?next=/co/")
    elif server_name == "local":
        driver.get("http://localhost:8000/")
    elif server_name == "staging":
        driver.get("https://staging.optimile-dev.eu/")

    request.cls.driver = driver
    yield
    shutil.rmtree(cache_directory)
    driver.close()


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
    path = screenshot_directory.format(name)
    driver.get_screenshot_as_file(path)
