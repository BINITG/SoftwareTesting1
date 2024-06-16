from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

import time
driver.implicitly_wait(10)

driver.get("https://classic.crmpro.com")
driver.maximize_window()

'''PERFORMING LOGIN BY USING ACTIONCHAINS'''

k=driver.find_element(By.NAME,"username")
p=driver.find_element(By.NAME,"password")
m=driver.find_element(By.XPATH,'//input[@class="btn btn-small"]')

N=ActionChains(driver)
N.send_keys_to_element(k,'batchautomation')
N.send_keys_to_element(p,'Test@12345')
N.click(m).perform()
time.sleep(3)

