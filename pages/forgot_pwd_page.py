from selenium.webdriver.common.by import By
from pages.base_page import Basepage
from time import sleep
class Forgot_Pwd_Page(Basepage):
    Email_Input = (By.XPATH, f'//input[@placeholder="Enter your email"]')
    Invalid_Email_MESSAGE = (By.XPATH, f'//p[contains(text(),"Please enter a valid email address!")')
    SEND_EMAIL_BUTTON =(By.XPATH, '//*[@id="root"]/div/div[2]/button')
    Back_To_Login=(By.LINK_TEXT, "Back to login")

    def set_email(self, email):
        self.wait_for_elem(*self.Email_Input)
        self.chrome.find_element(*self.Email_Input).send_keys(email)
        sleep(1)

    def clik_send_emial_button(self):
        self.chrome.find_element(*self.SEND_EMAIL_BUTTON).click()

    def click_back_to_login(self):
        self.chrome.find_element(*self.Back_To_Login).click()

    def verify_error_message(self):
        excepted= "Please enter a valid email adrdress"
        actual = self.chrome.find_element(*self.Invalid_Email_MESSAGE).text
        self.assertEqual(excepted,actual,'The message by the page is incorect')