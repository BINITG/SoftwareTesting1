from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(5)
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.quit()