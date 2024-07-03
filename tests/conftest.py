import pytest
from utils.selenium_testcontainers import SeleniumContainer

@pytest.fixture(scope="class", autouse=True)
def setup_and_teardown():
    print("Config")
    container = SeleniumContainer()
    container.create()
    yield
    container.qiute()
    print("Teardown after test")
    
    
