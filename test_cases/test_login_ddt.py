# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# from page_objects.Login_Page import Login
# from utilities import XLutils
#
#
# class Test_CredKart_Login_DDT:
#     XLPath = "F:\Credence- CT14 batch\Python-Automation (July_Month)\Framework - Tushar Sir\LoginTest-copy.xlsx"
#
#     def test_CredKart_Login_ddt_006(self, setup):
#         self.driver = setup
#         self.lp = Login(self.driver)
#         self.row = XLutils.RowCount(self.XLPath, "Sheet1")
#         print("No of rows in excel is : " + str(self.row))
#         Login_Status_List = []
#
#         for r in range(2, self.row + 1):
#             self.email = XLutils.ReadData(self.XLPath, "Sheet1", r, 2)
#             self.password = XLutils.ReadData(self.XLPath, "Sheet1", r, 3)
#             self.exp_result = XLutils.ReadData(self.XLPath, "Sheet1", r, 4)
#
#             self.lp.Login_URL()
#             self.lp.Enter_Email(self.email)
#             self.lp.Enter_Password(self.password)
#             self.lp.CLick_Login_Button()
#             if self.lp.Login_Status() == True:
#                 if self.exp_result == "Pass":
#                     Login_Status_List.append("Pass")
#                     self.driver.save_screenshot(".\\ScreenShots\\SS_DDT_pass.PNG")
#                     self.lp.CLick_Menu_Button()
#                     self.lp.CLick_Logout_Button()
#                     XLutils.WriteData(self.XLPath, "Sheet1", r, 5, "PASS")
#                 elif self.exp_result == "Fail":
#                     Login_Status_List.append("Fail")
#                     self.driver.save_screenshot(".\\ScreenShots\\SS_DDT_fail.PNG")
#                     self.lp.CLick_Menu_Button()
#                     self.lp.CLick_Logout_Button()
#                     XLutils.WriteData(self.XLPath, "Sheet1", r, 5, "FAIL")
#             if self.lp.Login_Status() == False:
#                 if self.exp_result == "Pass":
#                     Login_Status_List.append("Fail")
#                     self.driver.save_screenshot(".\\ScreenShots\\SS_DDT_fail")
#                     XLutils.WriteData(self.XLPath, "Sheet1", r, 5, "FAIL")
#                 elif self.exp_result == "Fail":
#                     Login_Status_List.append("Pass")
#                     XLutils.WriteData(self.XLPath, "Sheet1", r, 5, "PASS")
#
#         print(Login_Status_List)
#
#         if "Fail" not in Login_Status_List:
#             assert True
#         else:
#             assert False
