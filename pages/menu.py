from selenium.webdriver.common.by import By

class Menu:
    def __init__(self,driver) -> None:
        self.driver = driver
        self.register_page = '//a[text()="Register"]'        

    def go_to_registraion_page(self):
        self.driver.find_element(By.XPATH, self.register_page).click()