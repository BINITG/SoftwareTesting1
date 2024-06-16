from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

import time
driver.implicitly_wait(10)

driver.get("https://www.freshworks.com/")
driver.maximize_window()

header_element=driver.find_element(By.TAG_NAME,'h1')
print(header_element.text)