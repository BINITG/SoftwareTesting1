from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.implicitly_wait(10)
import time


driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

#type='file'
driver.find_element(By.NAME,'upfile').send_keys('D:\BINIT KUMAR CV.pdf')
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)
