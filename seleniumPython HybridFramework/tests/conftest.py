import pytest
import pytest_html
from selenium import webdriver

from utilites import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info","browser")
    driver = None
    if browser.__eq__("edge"):
         driver = webdriver.Edge()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        print("Provide a valid browser name from this list edge/chrome/firefox")


    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("basic info","url")
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()



 