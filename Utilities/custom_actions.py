from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from Testcases.conftest import setup

def Click_banner(setup, ban_ele, slider_ele):
    global Banner_webele
    driver=setup
    wait= WebDriverWait(driver,30,3)
    action = ActionChains(driver)
    try:
        web_ele = wait.until(EC.visibility_of_element_located(('xpath', ban_ele)))
        web_ele.click()
    except:
        driver.find_element('xpath',slider_ele).click()
        web_ele =wait.until(EC.visibility_of_element_located(('xpath',ban_ele)))
        web_ele.click()

def scroll_to_element(setup,element):
    driver = setup
    action = ActionChains(driver)
    webelement =driver.find_element('xpath',element)
    action.scroll_to_element(webelement)




