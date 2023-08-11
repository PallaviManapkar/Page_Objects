# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# from page_objects.Login_Page import Login
# from page_objects.Checkout_Page import Credkart_checkout
#
# class Test_Credkart_Checkout:
#     def test_checkout(self,setup):
#         self.driver = setup
#         self.lp = Login(self.driver)
#         self.lp.Login_URL()
#         self.lp.Enter_Email("Credencetest@test.com")
#         self.lp.Enter_Password("Credence@123")
#         self.lp.CLick_Login_Button()
#         # Click on Product--Macbook
#         self.cop = Credkart_checkout(self.driver)
#         self.cop.CLICK_MACBOOK()
#         # Click on add to cart
#         self.cop.CLICK_ADD_TO_CART()
#         # Proceed to Checkout
#         self.cop.CLICK_PROCEED_TO_CHECKOUT()
#         time.sleep(3)
#         # Enter First_Name
#         self.cop.ENTER_FIRST_NAME('Pallavi')
#         # Enter Last_Name
#         self.cop.ENTER_LAST_NAME('Pune')
#         # Enter Phone
#         self.cop.ENTER_PHONE_NUMBER(9145107610)
#         # Enter Address
#         self.cop.ENTER_ADDRESS("Dhankawadi,PUNE")
#         # Enter Zip
#         self.cop.ENTER_ZIP(411013)
#         # Select state
#         # state = 'Pune'
#         self.cop.DROPDOWN_STATE('Pune')
#         # state = Select(self.driver.find_element(By.XPATH, "//select[@id='state']"))
#         # state.select_by_visible_text("Pune")
#         # Enter  Owner name
#         self.cop.ENTER_OWNER_NAME('PALLAVI')
#         # Enter CVV
#         self.cop.ENTER_CVV("043")
#         # Select Year
#         self.cop.DROPDOWN_YEAR()
#
#         # Select Month
#         self.cop.DROPDOWN_MONTH()
#
#         # Enter card number\
#         # 5281 0370 4891 6168
#         self.cop.ENTER_CARD_NUMBER('5281')
#         self.cop.ENTER_CARD_NUMBER('0370')
#         self.cop.ENTER_CARD_NUMBER('4891')
#         self.cop.ENTER_CARD_NUMBER('6168')
#
#         # Click on Checkout button
#         self.cop.CLICK_CHECKOUT()
#         self.cop.SUCCESS_MESSAGE()
#         # print(self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]").text)
#
#
#
#
#
#
