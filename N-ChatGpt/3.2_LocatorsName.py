from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
import time
driver.implicitly_wait(10)

driver.get("https://www.crmpro.com/login.cfm")
driver.maximize_window()

driver.find_element(By.XPATH,'//input[@name="username"]').send_keys('batchautomation')
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('Test@12345')
driver.find_element(By.XPATH,'//input[@value="Login"]').click()
time.sleep(4)

