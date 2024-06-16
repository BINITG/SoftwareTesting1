from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

#windowid=driver.current_window_handle
#print(windowid) #D69DC4B11263E3F968EC0921F4CA2759
                #E21000DF0A60DEB5A14D1DED78C328A6

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowIDs=driver.window_handles

#APPROACH1
parentwindowid=windowIDs[0] #A2C86925531334A1E91A0C8646C83F87
childwindowid=windowIDs[1]  #826A8E1DE24F2B58AD7B22B4A6E0EB37

#print(parentwindowid,childwindowid)

#driver.switch_to.window(childwindowid)
#print("title of the child window:",driver.title)

#driver.switch_to.window(parentwindowid)
#print("title of the child window:",driver.title)

#APPROACH2
for winid in windowIDs:
    driver.switch_to.window(winid)
    print(driver.title)

time.sleep(3)
for winid in windowIDs:
    driver.switch_to.window(winid)
    if driver.title==OrangeHRM or driver.title=='xyz':
        driver.close()