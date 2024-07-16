class IndexPage:
    
    def __init__(self, browser, url) -> None:
        self.browser = browser
        self.url = url
        
        
    def go_to_main_page(self):
        self.browser.get(self.url)
    
    