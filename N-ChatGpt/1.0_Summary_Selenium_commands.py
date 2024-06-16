from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver=webdriver.Chrome()

import time
import xlrd

driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)                                    #MAX TIME IS 10S...SO IF ELEMENT CAN BE FOUND IN 5 SEC
wait.until(ec.title_is('Hubspot Login'))                         #EXPLICIT WAIT CONDITION-1
email_id=wait.until(ec.presence_of_element_located((By.ID,"username")))  #EXPLICIT WAIT CONDITION-2

driver.execute_script("window.scrollBy(0,1000)")                             #SCROLL DOWN BY PIXEL
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")     #SCROLL DOWN TO END OF PAGE
driver.execute_script("arguments[0].scrollIntoView();",flag)                 #SCROLL DOWN TO PARTILCULAR ELEMENT


from selenium.webdriver.support.ui import Select
k=Select(driver.find_element(By.ID,"Form_getForm_Country"))
k.select_by_visible_text('Andorra')                                        #SELECT BY VISIBLE TEXT
k.select_by_value("Fiji")                                                  #SELECT BY VALUE
k.select_by_index("10")                                                    #SELECT BY INDEX

'''move to element'''
from selenium.webdriver import ActionChains
ActionChains(driver).move_to_element(element).perform()                   #MOUSE-HOVERING

ActionChains(driver).drag_and_drop(source-element,target-element).perform() #DRAG AND DROP
ActionChains(driver).click_and_hold(source-element).move_to_element(target-element).release().perform() #DRAG-DROP

ActionChains(driver).context_click(element).perform()              #RIGHT-CLICK

driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
driver.switch_to.default_content()

driver.switch_to.frame(2)                                        #BY ID
driver.switch_to.frame('main')                                   #BY NAME

driver.find_element(By.NAME,'UPLOAD-BUTTON').send_keys('FILE-LOCATION')
driver.find_element(By.XPATH,"SUBMIT-BUTTON").click()

driver.back()
driver.forward()
driver.refresh()

print(driver.get_cookies())
driver.add_cookie({"name":"naveenpython","domain":"reddit.com","value":"python"})

driver.get_screenshot_as_file('reddit.png')    #METHOD-1 TO TAKE SCREENSHOT
driver.save_screenshot('Binit.jpeg')            #METHOD-2 TO TAKE SCREESHOT



