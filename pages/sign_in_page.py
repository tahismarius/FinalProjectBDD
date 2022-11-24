from selenium.webdriver.common.by import By
from pages.base_page import Basepage
#sectiune de identificare
class Sign_In_Page(Basepage):
    EMAIL_INPUT = (By.XPATH, f'//input[@placeholder="Enter your email"]')
    PASS_INPUT = (By.XPATH, f'//input[@placeholder="Enter your password"]')
    LOGIN_BUTTONS = (By.XPATH, '//button[@type="submit"]')
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot password?")


    def navigate_to_sign_in_page(self):
        self.chrome.get("https://jules.app/sign-in")

    def set_email(self, email):
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_pwd(self, password):
        self.chrome.find_element(*self.PASS_INPUT).send_keys(password)

    def click_button_logg_in(self):
        self.chrome.find_element(*self.LOGIN_BUTTONS).click()

    def click_forgot_pwd_link(self):
        self.chrome.find_element(*self.FORGOT_PASSWORD_LINK).click()

    def check_curent_url(self):
        actual_url = self.chrome.current_url
        expected_url = 'https://jules.app/'
        self.assertEqual(actual_url,expected_url, "The URL doesn't match")



