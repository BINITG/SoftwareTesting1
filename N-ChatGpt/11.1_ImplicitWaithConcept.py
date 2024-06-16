from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

#driver.implicitly_wait(10)
import time



driver.get("https://app.hubspot.com/login")
driver.maximize_window()

print(driver.title)

driver.find_element(By.ID,"username").send_keys("test@gmail.com")
driver.find_element(By.ID,"password").send_keys("test@12345")

#driver.implicitly_wait(0) #nullify of imp wait
#e3
#e4
#e5


#time out=10==PAUSING SCRIPT FOR 10 SEC===NO SUCH ELEMEN EXCEPTION WILL BE THROWN.
#IT IS A Dynamic wait==BOTH EXPLICIT AND IMPLICIT WAIT ARE DYNAMIC WAIT.
#IMPLICIT wait will be applied for all the web elements.
#Global wait==IMPLICIT WAIT IS GLOBAL WAIT BUT EXPLIICIT WAIT IS NOT A GLOBAL WAIT.
#find_element
#find_elements
#only for web elements
#Not for non-web elements:title,url,alerts