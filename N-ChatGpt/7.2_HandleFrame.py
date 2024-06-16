from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.implicitly_wait(10)
import time

driver.get("http://londonfreelance.org/courses/frames/index.html")

#driver.switch_to.frame(2)                                 #INDEX VALUE(0,1,2,...)--CONFUSING METHOD
#driver.switch_to.frame('main')                            #NAME/ID----------------GOOD TO USE
frame_element=driver.find_element(By.NAME,'main')          #BY CREATING FRAME ELEMENT AND THEN SWITCH TO IT--GOOD
driver.switch_to.frame(frame_element)

headervalue=driver.find_element(By.CSS_SELECTOR,'body>h2').text
print(headervalue)

driver.switch_to.default_content()                         #SWITCH TO DEFAULT CONTENT
driver.switch_to.parent_frame()                            #SWITCH TO PARENT FRAME

