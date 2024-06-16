from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[text()='OrangeHM, Inc']").click()
time.sleep(5)

driver.close()
driver.quit()