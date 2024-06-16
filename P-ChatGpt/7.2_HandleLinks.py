from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
import time

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(3)

#CLICK ON LINK
#driver.find_element(By.LINK_TEXT," Digital downloads ").click()
#driver.find_element(By.PARTIAL_LINK_TEXT," Digital").click()

#FIND NUMBER OF LINKS IN A PAGE
links=driver.find_elements(By.TAG_NAME,"a")
print("total number of links:",len(links))

#print all thr link names
for link in links:
    print(link.text)