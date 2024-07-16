from pytest_bdd import given
from configuration.config import Configuration
from utils.selenium_testcontainers import SeleniumContainer
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest

@pytest.fixture(scope="session", autouse=True)
def browser():
    print("Config")
    container = SeleniumContainer()
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