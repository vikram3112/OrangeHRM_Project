import time
import allure
from pageObjects.LoginPage import OrangeHRM_Login
from utilities.Logger import LogGenerator
from allure_commons.types import AttachmentType
from allure_commons.types import AttachmentType
from utilities.ReadConfig import Readconfig


class Test_Login:
    log = LogGenerator.loggen()
    Username = Readconfig.GetUserName()
    Password = Readconfig.GetPassword()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Page Title Test Case")
    @allure.link("https://opensource-demo.orangehrmlive.com/")
    @allure.story("This is Story")
    def test_pagetitle(self,setup):
        self.log.info("TestCase Pagetitle is started")
        self.log.info("opening browser")
        self.driver = setup
        self.log.info("Page Title is : " + self.driver.title)
        if self.driver.title == "OrangeHRM":
            self.log.info("Taking screenshot")
            time.sleep(4)
            allure.attach(self.driver.get_screenshot_as_png(), name="test_page_title_001_pass", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("C:\\Users\\Dreamer\\Documents\\pythonProject1\\pythonProject\\OrangeHRM Project\\Screenshots\\Test_title_pass.png")
            self.driver.close()
            self.log.info("Test Case test_pagetitle is passed")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Dreamer\\Documents\\pythonProject1\\pythonProject\\OrangeHRM Project\\Screenshots\\Test_title_fail.png")
            self.driver.close()
            self.log.info("Test Case test_pagetitle is Failed")
            assert False



    def test_login_002(self, setup):
        self.log.info("test case test_login_002 is Started")
        self.log.info("Opening Browser")
        self.driver = setup
        self.lp = OrangeHRM_Login(self.driver)
        self.log.info("Entering Username :"+ self.Username)
        self.lp.Enter_Username("Admin")
        self.log.info("Entering Password :"+ self.Password)
        self.lp.Enter_Password("admin123")
        time.sleep(4)
        self.log.info("Clicking in Login Button")
        self.lp.Click_Login()
        time.sleep(4)
        self.log.info("Clicking on Menu Button")
        self.lp.Click_Menu()
        time.sleep(5)
        self.log.info("Clicking on Logout Button")
        self.lp.Click_Logout()






        # if self.lp.Login_Status() == True:
        #     # self.log.info("taking screenshot")
        #     self.driver.save_screenshot("C:\\Users\\Dreamer\\Documents\\pythonProject1\\pythonProject\\OrangeHRM Project\\Screenshots\\test_page_title_001_pass.png")
        #
        #     # self.log.info("Clicking on Menu button")
        #     self.lp.Click_Menu()
        #     # self.log.info("Clicking on logout button")
        #     self.lp.Click_Logout()
        #     self.driver.close()
        #     # self.log.info("Testcase test_login_002 is passed")
        #     assert True
        # else:
        #     self.driver.save_screenshot("C:\\Users\\Dreamer\\Documents\\pythonProject1\\pythonProject\\OrangeHRM Project\\Screenshots\\test_page_title_001_fail.png")
        #     self.driver.close()
        #     # self.log.info("Testcase test_login_002 is failed")
        #     assert False

# pytest -v -n=2 --html=Reports/OrangeHRMreport.html --alluredir="Allure-results"