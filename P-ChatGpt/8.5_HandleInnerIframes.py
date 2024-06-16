from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")

driver.switch_to.parent_frame()#DIRECTLY SWITCH TO PARENT FRAME(OUTER FRAME)
