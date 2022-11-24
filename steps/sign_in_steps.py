from behave import *
# Given, When , And, But, Than -> Gherkin Syntax
# Given seteaza situatia curenta
# When definste pasi din test
#Then efectueaza verificarea testului

@Given('sign_in: I am a user on Jules sign in page')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()

@When('sign_in: I set my email to "{email}"')
def step_impl(context, email):
    context.sign_in_page.set_email(email)

@When('sign_in: I set my password to "{password}"')
def step_impl(context, password):
    context.sign_in_page.set_pwd(password)

@when('sign_in: I click the loggin button')
def step_impl(context):
    context.sign_in_page.click_button_logg_in()

@When('sign_in: I click the forgot password link')
def step_impl(context):
    context.sign_in_page.click_forgot_pwd_link()

@Then('sign_in: I am returned to the home page')
def step_impl(context):
    context.sign_in_page.check_curent_url()