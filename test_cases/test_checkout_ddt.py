#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from page_objects.Login_Page import Login
# from page_objects.Checkout_Page import Credkart_checkout
# from utilities import XLutils
#
# class Test_Credkart_Checkout_DDT():
#     XLpath = "F:\Credence- CT14 batch\Python-Automation (July_Month)\Framework - Tushar Sir\LoginTest-copy.xlsx"
#
#     def test_credkart_checkout_ddt_007(self,setup):
#         self.driver = setup
#         self.lp = Login(self.driver)
#         self.lp.Login_URL()
#         self.lp.Enter_Email("Credencetest@test.com")
#         self.lp.Enter_Password("Credence@123")
#         self.lp.CLick_Login_Button()
#         self.cop = Credkart_checkout(self.driver)
#         self.cop.CLICK_MACBOOK()
#         self.cop.CLICK_ADD_TO_CART()
#         self.cop.CLICK_PROCEED_TO_CHECKOUT()
#         self.cop.
#
