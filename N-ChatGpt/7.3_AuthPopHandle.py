from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.implicitly_wait(10)
import time


driver.get("http://the-internet.herokuapp.com/basic_auth")               #ASKING FOR USERNAME/PASSWORD TO OPEN URL
time.sleep(3)

driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")    #IN URL, WE CAN PROVIDE USERNAME/PASSWORD
time.sleep(3)
