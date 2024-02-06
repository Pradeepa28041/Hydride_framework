from time import sleep
from selenium import webdriver
from Pageobject.HomeLogin import login_Page,home_banners
import pytest
from selenium.webdriver.chrome.options import Options
from Utilities.readproperty import Readconfig
from Utilities.customLog import Loggin


class Test001Login:
    url = Readconfig.getapplication_URL()
    mobile_no = Readconfig.get_mobile_no()
    otp_no = Readconfig.get_otp()
    title = Readconfig.getapplication_title()
    logger = Loggin.loggin()

    def test_verify_homepage(self, setup):
        self.logger.info("***************Test001Login*****************")
        self.logger.info("***************verify_homepage***************")
        self.driver = setup
        self.driver.get(self.url)
        sleep(3)
        self.driver.refresh()
        self.lp = login_Page(self.driver)
        self.lp.verify_button()
        act_title = self.driver.title
        if self.title == act_title:
            self.driver.save_screenshot(filename= ".\\Screenshot\\test_login_passimg.png")
            assert True
            self.driver.close()
            self.logger.info("***************verified_homepage***************")

        else:
            self.driver.save_screenshot(".\\Screenshot\\defect.png")
            self.logger.info("***************verified_homepage_Failed***************")
            assert False

    def test_login(self, setup):
        self.logger.info("***************test_login_started***************")
        self.driver = setup
        self.driver.get(self.url)
        sleep(5)
        self.driver.refresh()
        self.lp = login_Page(self.driver)
        # self.lp.Shadow_root()
        self.lp.mouse_login()
        self.lp.click_login()
        self.lp.enter_number(self.mobile_no)
        self.lp.getotp()
        self.lp.enter_otp(self.otp_no)
        self.lp.verify_otp()
        self.ban3=home_banners(self.driver)
        self.ban3.banners()

        act_title = self.driver.title
        if self.title == act_title:
            self.driver.save_screenshot(".\\Screenshot\\test_login_passimg.png")
            self.logger.info("***************successfully_login***************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshot\\defect.png")
            self.logger.info("***************Login_failed***************")
            assert False


