 #we need to install requests package through File->settings->ProjectInterpreter->+->requests

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
import time

driver.get("http://www.deadlinkcity.com/errorlist.asp")
driver.maximize_window()
time.sleep(3)

alllinks=driver.find_elements(By.TAG_NAME,"a")
count=0

for link in alllinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url,"is broken link")
        count+=1
    else:
        print(url,"is valid link")
print("Total number of broken links:",count)