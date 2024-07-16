from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class RegistrationPage:
    
    def __init__(self, driver) -> None:
        self.dirver = driver
        self.registration_form = "rightPanel"
        self.first_name = "first-name id"
        self.last_name = "last-name id"
        self.address = "address id"
        self.state = "state id"
        self.zip_code = "zip code id"
        self.phone = "phone"
        self.ssn = "ssn"
        
        self.username = "username"
        self.password = "password"
        self.confirm_password = "confirm button"
        self.registraion_button = "registraion button"
        
    def wait_for_form_to_be_visible(self):
        
        element = WebDriverWait(self.dirver,10)\
            .until(lambda x: x.find_element(By.ID,self.registration_form))
            
        return element.is_displayed()
    

    
    

