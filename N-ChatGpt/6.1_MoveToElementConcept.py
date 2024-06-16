from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

import time
driver.implicitly_wait(10)

driver.get("https://artoftesting.com/")
driver.maximize_window()
time.sleep(3)

'''move to element'''
k=driver.find_element(By.XPATH,"//a[text()='Manual']")
ActionChains(driver).move_to_element(k).perform()


M=driver.find_element(By.XPATH,"//a[text()='What is Manual Testing?']")
M.click()


