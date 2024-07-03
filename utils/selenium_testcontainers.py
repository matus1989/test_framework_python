from testcontainers.selenium import BrowserWebDriverContainer
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver

class SeleniumContainer:
    
    def __init__(self) -> None:
        self.web_driver = None

    def create(self) -> webdriver:
        """
        Create driver instance
        
        Returns:
        BrowserWebDriverContainer: return instance of WebDriverContainer
        
        """
        
        with BrowserWebDriverContainer(DesiredCapabilities.CHROME) as chrome:
            self.web_driver = chrome.get_driver()
        return self.web_driver
    
    def qiute(self) -> None:
        """
        Quite webdriver and close web browser 
        """
        if self.web_driver:
            self.web_driver.quit