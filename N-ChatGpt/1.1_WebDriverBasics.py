from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

import time
driver.implicitly_wait(5)

driver.get('https://www.google.com/')
print(driver.title)

driver.find_element(By.ID,"APjFqb").send_keys('naveen automationlabs')
optionlist=driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
print(len(optionlist))

for ele in optionlist:
    print(ele.text)
    if ele.text=='naveen automationlabs youtube':
         ele.click()
         break

time.sleep(5)
driver.quit()


driver.quit()