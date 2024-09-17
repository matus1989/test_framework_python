from pytest_bdd import scenarios,scenario, parsers
from pytest_bdd import given, when, then
from pages.menu import Menu
from pages.registraion_page import RegistrationPage
scenarios('../features/registration.feature')


@given('I am on the registration page')
def open_registraion_page(browser):
    menu = Menu(browser)
    menu.go_to_registraion_page()
    
    registrationPage = RegistrationPage(browser)
    registrationPage.wait_for_form_to_be_visible()


@given(parsers.cfparse('I write first name "{name}"'))
def fill_first_name_input(browser,name):
    registration = RegistrationPage(browser)
    registration.send_keys_to_first_name(name)
    