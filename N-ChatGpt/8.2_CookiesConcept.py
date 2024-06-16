from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.implicitly_wait(10)
import time

driver.get("https://www.reddit.com/")
driver.maximize_window()

print(driver.get_cookies())                                                        #PRINT ALL COOKIES

driver.add_cookie({"name":"naveenpython","domain":"reddit.com","value":"python"}) #ADD COOKIES

print(driver.get_cookies())                                                       #PRINT ADDED COOKIES

#cookies=driver.get_cookies()                                                     #DECLARING AND CALLING COOKIES
#for i in Cookies:                                                 #PRINTING COOKIES USING FOR LOOP
#    print(i)

