from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
import time
driver.get("https://www.orangehrm.com/")
time.sleep(5)

whyorangehrm=driver.find_element(By.XPATH,"//a[text()='Why OrangeHRM']")
ourcustomers=driver.find_element(By.XPATH,"//div[@class='secondary secondary-menu-3']//li[1]")
casestudies=driver.find_element(By.XPATH,"//h6[@class='list-sub-menu-title']//a[normalize-space()='Case Studies']")

#MOUSEHOVER
act=ActionChains(driver)
act.move_to_element(whyorangehrm).move_to_element(ourcustomers).move_to_element(casestudies).click()