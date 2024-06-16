from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

import time
driver.implicitly_wait(10)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

''' right/context click'''

right_click_ele=driver.find_element(By.XPATH,"//span[text()='right click me']")
ActionChains(driver).context_click(right_click_ele).perform()
time.sleep(5)

right_click_options=driver.find_elements(By.CSS_SELECTOR,'li.context-menu-icon span')
for k in right_click_options:
    print(k.text)
    if k.text=='copy':
        k.click()
        break