from testcontainers.selenium import BrowserWebDriverContainer
from testcontainers.selenium import wait_container_is_ready
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

class SeleniumContainer:
    
    def __init__(self, browser='firefox') -> None:
        self.container = None
        self.driver = None
        self.browser = browser
    
    @wait_container_is_ready(120)
    def create(self) -> webdriver:
        """
        Create driver instance
        
        Returns:
        BrowserWebDriverContainer: return instance of WebDriverContainer
        
        """
        try:
            self.container = BrowserWebDriverContainer(self.desired_capabilities_browser())
            self.container.start()
            self.driver = self.container.get_driver()
        except Exception as e:
            print(f"An error occured: {e}")    
        return self.driver
    
    def qiute(self) -> None:
        """
        Quite webdriver and close web browser 
        """
        if self.driver:
            self.driver.quit()
        self.container.stop()
    
    def desired_capabilities_browser(self) -> DesiredCapabilities:
        if self.browser == 'firefox':
            return DesiredCapabilities.FIREFOX.copy()
        elif self.browser == 'chrome':
            return DesiredCapabilities.CHROME.copy()