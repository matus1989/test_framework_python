from pytest_bdd import given
from configuration.config import Configuration
from utils.selenium_testcontainers import SeleniumContainer
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="firefox",help="Browser to run tests on")


# def pytest_generate_tests(metafunc):
#     if "browser" in metafunc.fixturenames:
#         metafunc.parametrize("browser", metafunc.config.getoption("browser"))

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    borwser_option = request.config.getoption("browser")
    print(borwser_option)

    container = SeleniumContainer(borwser_option)
    driver = container.create()
    yield driver
    container.qiute()

   

@pytest.fixture(scope="session",autouse=True)
def url():
    conf = Configuration()
    yield conf.url

   
@given("I am on main bank main page")
def main_page(browser,url):
    print("-----------------------------------------------------")
    print (url) 
    print("-----------------------------------------------------")
    browser.get(url)
    print(browser.title)
    print("-----------------------------------------------------")