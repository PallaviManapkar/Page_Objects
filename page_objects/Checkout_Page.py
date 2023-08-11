import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class Credkart_checkout():
    click_product_macbook_XPATH = (By.XPATH,"/html/body/div/div[2]/div[3]/div/div/a[2]/h3")
    click_Add_to_cart_XPATH = (By.XPATH,"//input[@value='Add to Cart']")
    click_proceed_to_checkout_XPATH = (By.XPATH,"//a[@class='btn btn-success btn-lg']")
    enter_first_name_XPATH = (By.XPATH,"//input[@id='first_name']")
    enter_last_name_XPATH = (By.XPATH,"//input[@id='last_name']")
    enter_phone_number_XPATH = (By.XPATH,"//input[@id='phone']")
    enter_address_XPATH = (By.XPATH,"//textarea[@id='address']")
    enter_zip_XPATH = (By.XPATH,"//input[@id='zip']")
    dropdown_state_XPATH = (By.XPATH,"//select[@id='state']")
    enter_owner_name_XPATH = (By.XPATH,"//input[@id='owner']")
    enter_cvv_XPATH = (By.XPATH,"//input[@id='cvv']")
    dropdown_year_XPATH = (By.XPATH,"//select[@id='exp_year']")
    dropdown_month_XPATH = (By.XPATH,"//select[@id='exp_month']")
    enter_card_number_XPATH = (By.XPATH,"//input[@id='cardNumber']")
    click_checkout_XPATH = (By.XPATH,"//button[@id='confirm-purchase']")
    success_message_XPATH = (By.XPATH,"/html/body/div/div[1]/p[1]")

    def __init__(self,driver):
        self.driver = driver

    def CLICK_MACBOOK(self):
        self.driver.find_element(*Credkart_checkout.click_product_macbook_XPATH).click()

    def CLICK_ADD_TO_CART(self):
        self.driver.find_element(*Credkart_checkout.click_Add_to_cart_XPATH).click()

    def CLICK_PROCEED_TO_CHECKOUT(self):
        self.driver.find_element(*Credkart_checkout.click_proceed_to_checkout_XPATH).click()

    def ENTER_FIRST_NAME(self,first_name):
        self.driver.find_element(*Credkart_checkout.enter_first_name_XPATH).send_keys(first_name)

    def ENTER_LAST_NAME(self,last_name):
        self.driver.find_element(*Credkart_checkout.enter_last_name_XPATH).send_keys(last_name)

    def ENTER_PHONE_NUMBER(self,phone_number):
        self.driver.find_element(*Credkart_checkout.enter_phone_number_XPATH).send_keys(phone_number)

    def ENTER_ADDRESS(self,address):
        self.driver.find_element(*Credkart_checkout.enter_address_XPATH).send_keys(address)

    def ENTER_ZIP(self,zip):
        self.driver.find_element(*Credkart_checkout.enter_zip_XPATH).send_keys(zip)

    def DROPDOWN_STATE(self,state):
        state = Select(self.driver.find_element(*Credkart_checkout.dropdown_state_XPATH))
        state.select_by_visible_text('Pune')
        time.sleep(3)

    def ENTER_OWNER_NAME(self,owner_name):
        self.driver.find_element(*Credkart_checkout.enter_owner_name_XPATH).send_keys(owner_name)

    def ENTER_CVV(self,cvv):
        self.driver.find_element(*Credkart_checkout.enter_cvv_XPATH).send_keys(cvv)

    def DROPDOWN_YEAR(self):
        year = Select(self.driver.find_element(*Credkart_checkout.dropdown_year_XPATH))
        year.select_by_index(2)

    def DROPDOWN_MONTH(self):
        month = Select(self.driver.find_element(*Credkart_checkout.dropdown_month_XPATH))
        month.select_by_index(2)

    def ENTER_CARD_NUMBER(self,card_number):
        self.driver.find_element(*Credkart_checkout.enter_card_number_XPATH).send_keys(card_number)
        time.sleep(3)

    def CLICK_CHECKOUT(self):
        self.driver.find_element(*Credkart_checkout.click_checkout_XPATH).click()
        time.sleep(3)

    def SUCCESS_MESSAGE(self):
        print(self.driver.find_element(*Credkart_checkout.success_message_XPATH).text)







