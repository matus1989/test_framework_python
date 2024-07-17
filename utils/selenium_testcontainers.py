from testcontainers.selenium import BrowserWebDriverContainer
from testcontainers.selenium import wait_container_is_ready
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

class SeleniumContainer:
    
    def __init__(self) -> None:
        self.firefox = None
        self.driver = None
    
    @wait_container_is_ready(120)
    def create(self) -> webdriver:
        """
        Create driver instance
        
        Returns:
        BrowserWebDriverContainer: return instance of WebDriverContainer
        
        """
        
        try:
            self.firefox = BrowserWebDriverContainer(DesiredCapabilities.FIREFOX.copy())
            self.firefox.start()
            self.driver = self.firefox.get_driver()
        except Exception as e:
            print(f"An error occured: {e}")    
        return self.driver
    
    def qiute(self) -> None:
        """
        Quite webdriver and close web browser 
        """
        if self.driver:
            self.driver.quit()
        self.firefox.stop()
            