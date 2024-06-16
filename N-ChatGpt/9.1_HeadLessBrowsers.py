from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.implicitly_wait(10)
import time

k="chrome"
if k=="chrome":
   options=webdriver.ChromeOptions
   options.headless=True
   driver=Webdriver.Chrome(options=options)


driver.get("http://amazon.in")
print(driver.title)

#WILL DO LATER...NOW IT'S NOT RUNNING...SOME WEBDRIVER ISSUE


