from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

import time
driver.implicitly_wait(10)

#driver.get("https://www.freshworks.com/")
driver.get("https://www.amazon.in/")
driver.maximize_window()

Linklist=driver.find_elements(By.TAG_NAME,'a')
print(len(Linklist))

for ele in Linklist:
    Link_text=ele.text
    print(Link_text)
    print(ele.get_attribute('href'))

imagelist=driver.find_elements(By.TAG_NAME,'img')
print(len(imagelist))

for ele in imagelist:
    print(ele.get_attribute('src'))


    #ok....everything is running properly