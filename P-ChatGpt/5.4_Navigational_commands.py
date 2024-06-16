from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time
driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.in/")

driver.back()#snapdeal
time.sleep(5)
driver.forward()#amazon
time.sleep(5)

driver.refresh()

driver.quit()
