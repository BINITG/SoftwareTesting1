from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
import time
driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.XPATH,'//textarea[@name="q"]')

searchbox.send_keys("selenium")
searchbox.submit()

#time.sleep(3)

driver.find_element(By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()