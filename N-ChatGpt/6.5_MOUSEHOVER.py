from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://artoftesting.com/")
time.sleep(3)

'''move to element'''
driver.find_element(By.XPATH,"//a[text()='Manual']").click()
time.sleep(15)