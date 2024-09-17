from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class RegistrationPage:

    def __init__(self, driver) -> None:
        self.dirver = driver
        self.registration_form = "rightPanel"
        self.first_name = "customer.firstName"
        self.last_name = "customer.lastName"
        self.address = "customer.address.streets"
        self.state = "customer.address.state"
        self.zip_code = "customer.address.zipCode"
        self.phone = "cusmtoemr.phoneNumber"
        self.ssn = "customer.ssn"

        self.username = "customer.username"
        self.password = "customer.password"
        self.confirm_password = "repeatedPassword"
        # <input type="submit" class="button" value="Register">
        self.registraion_button = "button"

    def wait_for_form_to_be_visible(self):

        element = WebDriverWait(self.dirver, 10)\
            .until(lambda x: x.find_element(By.ID, self.registration_form))

        return element.is_displayed()

    def send_keys_to_first_name(self, text):
        element = self.dirver.find_element(By.ID, self.first_name)
        element.send_keys(text)

        return self

    def send_keys_to_last_name(self, text):
        element = self.dirver.find_element(By.ID, self.last_name)
        element.send_keys(text)

        return self

    def send_keys_to_address(self, text):
        element = self.dirver.find_element(By.ID, self.address)
        element.send_keys(text)

        return self

    def send_keys_to_state(self, text):
        element = self.dirver.find_element(By.ID, self.state)
        element.send_keys(text)

        return self

    def send_keys_to_zip_code(self, text):
        element = self.dirver.find_element(By.ID, self.zip_code)
        element.send_keys(text)

        return self

    def send_keys_to_zip_code(self, text):
        element = self.dirver.find_element(By.ID, self.zip_code)
        element.send_keys(text)

        return self

    def send_keys_to_phone_number(self, text):
        element = self.dirver.find_element(By.ID, self.phone)
        element.send_keys(text)

        return self

    def send_keys_to_ssn(self, text):
        element = self.dirver.find_element(By.ID, self.ssn)
        element.send_keys(text)

        return self

    def send_keys_to_username(self, text):
        element = self.dirver.find_element(By.ID, self.username)
        element.send_keys(text)

        return self

    def send_keys_to_password(self, text):
        element = self.dirver.find_element(By.ID, self.password)
        element.send_keys(text)

        return self

    def send_keys_to_re_password(self, text):
        element = self.dirver.find_element(By.ID, self.confirm_password)
        element.send_keys(text)

        return self

    def click_register_button(self):
        self.dirver.find_element(
            By.CLASS_NAME, self.registraion_button).click()
