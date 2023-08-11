import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    Text_Email_XPATH = (By.XPATH, "//input[@name='email']")
    Text_Password_CSS = (By.CSS_SELECTOR, "input[id='password']")
    Click_Login_Button_XPATH = (By.XPATH, "//button[@type='submit']")
    login_status = (By.XPATH, "//h2[normalize-space()='CredKart']")
    CLick_Logout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")
    Click_Menu_XPATH = (By.XPATH, "//a[@role='button']")

    def __init__(self, driver):
          self.driver = driver


    def CLick_Menu_Button(self):
        self.driver.find_element(*Login.Click_Menu_XPATH).click()


    def CLick_Logout_Button(self):
        self.driver.find_element(*Login.CLick_Logout_XPATH).click()

    def Login_URL(self):
        self.driver.get("https://automation.credence.in/login")

    def Enter_Email(self, email):
        self.driver.find_element(*Login.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*Login.Text_Password_CSS).send_keys(password)

    def CLick_Login_Button(self):
        self.driver.find_element(*Login.Click_Login_Button_XPATH).click()

    def Login_Status(self):
        try:
            self.driver.find_element(*Login.login_status)
            return True
        except:
            return False



