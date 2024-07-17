from pytest_bdd import scenarios,scenario
from pytest_bdd import given
from pages.menu import Menu

scenarios('../features/registration.feature')


@given('I am on the registration page')
def open_registraion_page(browser):
    menu = Menu(browser)
    menu.go_to_registraion_page()
