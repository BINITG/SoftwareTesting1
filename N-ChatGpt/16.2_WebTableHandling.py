from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(15)

driver.get("https://seleniumpractise.blogspot.com/2021/08/")
driver.maximize_window()




#BY OTWANI