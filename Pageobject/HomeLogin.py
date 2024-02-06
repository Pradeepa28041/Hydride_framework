from time import sleep

from  selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Utilities.custom_actions import *
class login_Page:

    Home_Login_mouse="//span[.='log in']"
    L_login_button="//button[.='Log in / sign up']"
    M_number='//input[@name="mobile"]'
    Get_otp_button="//button[.='GET OTP']"
    Enter_otp='//input[@name="otp"]'
    verify_button="//button[.='VERIFY']"
    footer_about_us ="//p[.='ABOUT US']"
    def __init__(self,driver):
        self.driver=driver

    def Shadow_root(self):
        self.driver.implicitly_wait(10)
        shadow_host = self.driver.find_element('xpath','//div[@id="wzrkImageOnlyDiv"]')
        shadow_root_script=  "return arguments[0].shadowRoot"
        shadow_root = self.driver.execute_script(shadow_root_script, shadow_host)
        wait=WebDriverWait(self.driver,20)
        wait.until(EC.visibility_of_element_located(('xpath','//div[@id="close"]')))
        closepopup = shadow_root.find_element('xpath','//div[@id="close"]')
        closepopup.click()

    def mouse_login(self):
        action = ActionChains(self.driver, 30)
        login=self.driver.find_element('xpath',self.Home_Login_mouse)
        action.move_to_element(login).perform()

    def click_login(self,):
        self.driver.implicitly_wait(5)
        self.driver.find_element('xpath',self.L_login_button).click()

    def enter_number(self, mobile_no):
        self.driver.implicitly_wait(10)
        self.driver.find_element('xpath',self.M_number).send_keys(mobile_no)

    def getotp(self):
        self.driver.find_element('xpath',self.Get_otp_button).click()

    def enter_otp(self, otp_no):
        self.driver.find_element('xpath',self.Enter_otp).send_keys(otp_no)

    def verify_otp(self):
        self.driver.find_element('xpath', self.verify_button).click()

    def verify_footer(self,):
        scroll_to_element(self.driver,self.footer_about_us)


class home_banners:
    banner3 ='(//div[@class=" Carousel_link__MzK47"])[5]'
    slider = '(//div[@class="homepage-container"]//div[@class="swiper-button-next"])[1]'
    def __init__(self,driver):
        self.driver = driver
    def banners(self):
        Click_banner(self.driver,self.banner3,self.slider)
