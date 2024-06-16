from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
import time
driver.implicitly_wait(120)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drpcountry_ele=driver.find_element(By.XPATH,'//select[@id="input-country"]')
drpcountry=Select(drpcountry_ele)

#SELECT OPTION FROM THE DROPDOWN

#drpcountry.select_by_visible_text("India")
#drpcountry.select_by_value("10") #Argentina
#drpcountry.select_by_index(13)   #Index

#CAPTURE ALL THE OPTIONS AND PRINT THEM

alloptions=drpcountry.options
print("total number of options:",len(alloptions))
for opt in alloptions:
    print(opt.text)

#SELECT OPTION FROM DROPDOWN WITHOUT USING BUILT-IN METHOD

for opt in alloptions:
    if opt.text=="India":
        opt.click()
        break

alloptions=driver.find_elements(By.XPATH,'//*[@id="input-country"]/option')
print(len(alloptions))