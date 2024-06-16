from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.implicitly_wait(10)
import time

driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Best Sellers").click()
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.back()
time.sleep(2)

driver.refresh()

driver.quit()
