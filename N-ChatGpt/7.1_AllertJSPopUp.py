from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.implicitly_wait(10)
import time

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()

driver.find_element(By.NAME,'proceed').click()
time.sleep(3)

A=driver.switch_to.alert
print(A.text)
A.accept()                                 #accept it,Click on ok
A.dismiss()                                #cancel the pop up
A.send_keys('hi')                          #IF POP REQUIRES ANY INPUT VALUE
driver.switch_to.default_content()         #RETURN BACK TO PAGE AFTER POP-UP DIMISSSAL

time.sleep(3)
driver.quit()

