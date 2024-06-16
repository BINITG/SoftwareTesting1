from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

import time
driver.implicitly_wait(10)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.maximize_window()

print(driver.title)

driver.find_element(By.NAME,"subdomain").send_keys("BINIT")
driver.find_element(By.NAME,"Name").send_keys('Binitsingh')
driver.find_element(By.NAME,"Contact").send_keys('7979024390')
driver.find_element(By.NAME,"Email").send_keys('binitkumar.sgvu@gmail.com')
time.sleep(5)






