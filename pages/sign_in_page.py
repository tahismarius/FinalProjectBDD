from selenium.webdriver.common.by import By
from pages.base_page import Basepage

#sectiune de identificare
class Sign_In_Page(Basepage):


    Email_Input = (By.XPATH, f'//input[@placeholder="Enter your email"]')
    PWD_INPUT = (By.XPATH, f'//input[@placeholder="Enter your password"]')
    LOGIN_BUTTON = (By.XPATH , '//button[@type="submit"')
    FORGOT_PWD = (By.LINK_TEXT , "Forgot password" )



    def navigate_to_sign_in_page(self):
        self.chrome.get('https://jules.app/')

    def set_email(self, email):
        self.chrome.find_element(*self.Email_Input).send_keys(email)

    def set_pwd(self, passsword):
        self.chrome.find_element(*self.PWD_INPUT).send_keys(passsword)

    def click_button_logg_in(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def click_fgw_pwd_link(self):
        self.chrome.find_element(*self.FORGOT_PWD).click()

    def check_curent_url(self):
        actual_url=self.chrome.current_url
        expected_url = 'https://jules.app/'
        self.assertEqual(actual_url,expected_url, "The URL doesn't match")


