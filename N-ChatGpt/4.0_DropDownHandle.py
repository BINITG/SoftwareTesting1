from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()

import time
driver.implicitly_wait(15)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.maximize_window()

k=Select(driver.find_element(By.ID,"Form_getForm_Country"))

k.select_by_visible_text('Andorra')
time.sleep(4)

k.select_by_index('10')
time.sleep(4)

k.select_by_value('Canada')
time.sleep(4)







