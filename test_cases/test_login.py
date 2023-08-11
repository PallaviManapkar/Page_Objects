import pytest

# import warnings
# warnings.filterwarnings("ignore", message='not allowed')
# warnings.warn("not allowed")
# warnings.warn("warning: This is a warning message")

from selenium import webdriver
from selenium.webdriver.common.by import By

from page_objects.Login_Page import Login
from utilities.Logger import LogGenerator


class Test_CredKart_Login:
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_pageTitle_001(self, setup):
        self.driver = setup
        self.log.info("Started test case test_pageTitle_001 ")
        self.log.info("Opening the browser ")
        self.log.info("Checking the page-title : "+ self.driver.title)
        if self.driver.title == "CredKart":
            self.driver.save_screenshot(".\\ScreenSHots\\test_pageTitle_001_pass.PNG")
            self.log.info("Taking the Screenshot")
            self.driver.close()
            self.log.info("Testcase test_pageTitle_001 is PASSED ")
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenSHots\\test_pageTitle_001_fail.PNG")
            self.log.info("Taking the Screenshot ")
            self.driver.close()
            self.log.info("Testcase test_pageTitle_001 is FAILED ")
            assert False
#
    def test_CredKart_Login_002(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.log.info("Opening the browser")
        self.lp.Login_URL()
        self.log.info("Going to Launch the Url")
        self.log.info("Entering an Email : "+"Credencetest@test.com" )
        self.lp.Enter_Email("Credencetest@test.com")
        self.log.info("Entering the password : "+"Credence@123")
        self.lp.Enter_Password("Credence@123")
        self.log.info("Click on the LogIn Button")
        self.lp.CLick_Login_Button()
        self.log.info("Checking the Login Status : "+ str(self.lp.Login_Status()))
        # print(self.lp.Login_Status())

        if self.lp.Login_Status() == True:
            self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_pass.PNG")
            self.log.info("Taken Screenshot")
            self.log.info("Testcase test_CredKart_Login_002 is PASSED ")
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_fail.PNG")
            self.log.info("Taken Screenshot")
            self.log.info("Testcase test_CredKart_Login_002 is FAILED ")
            assert False

        # try:
        #     self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
        #     print("Login TestCase is Passed")
        #     self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_pass.PNG")
        #     self.driver.close()
        #
        #     assert True
        # except:
        #     print("Login TestCase is Failed")
        #     self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_fail.PNG")
        #     self.driver.close()
        #     assert False



# # 100s testcases--> if you have to run it in firefox
#
# # pytest -v --html=Reports/myreport.html --alluredir="AllureReports" -n=2  testCases/test_Login.py --browser chrome
