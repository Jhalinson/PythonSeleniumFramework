import pytest
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setUp(request):
    browser_name = request.config.getoption("--browser_name")
    global driver
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\jhali\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe",
            options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            executable_path="C:\\Users\\jhali\\Downloads\\geckodriver-v0.27.0-win64\\geckodriver.exe")
    elif browser_name == "IE":
        pass
        # driver = webdriver.Ie(
        #     executable_path="C:\\Users\\jhali\\Downloads\\IEDriverServer_x64_3.150.1\\IEDriverServer.exe",
        #     options=chrome_options)
    elif browser_name == "opera":
        pass
        # driver = webdriver.Opera(
        #     executable_path="C:\\Users\\jhali\\Downloads\\operadriver_win64\\operadriver_win64\\operadriver.exe",
        #     options=chrome_options)
    elif browser_name == "safari":
        pass
        # driver = webdriver.Safari(
        # executable_path="C:\\Users\\jhali\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe",
        # options=chrome_options)
    elif browser_name == "edge":
        pass
        # driver = webdriver.edge(
        #     executable_path="C:\\Users\\jhali\\Downloads\\edgedriver_win64\\msedgedriver.exe")

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
