from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver=webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[@href='/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles']").click()
driver.find_element(By.XPATH,"//span[text()='OnePlus Nord CE 3 Lite 5G (Chromatic Gray, 8GB RAM, 128GB Storage)']").click()
driver.find_element(By.XPATH,'//input[@id="add-to-cart-button"]').click()
