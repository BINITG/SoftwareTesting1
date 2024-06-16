from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
import time

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#select specific check box
driver.find_element(By.XPATH,'//input[@id="sunday"]').click()
time.sleep(4)

#select all the checkboxes
checkboxes=driver.find_elements(By.XPATH,'//input[@type="checkbox" and contains(@id,day)]')
print(len(checkboxes))

#approach1
for i in range(len(checkboxes)):
    checkboxes[i].click()

#approach2
for checkbox in checkboxes:
    checkbox.click()
#select multiple checkboxes by choice
for checkbox in checkboxes:
    dayname=checkbox.get_attribute('id')
    if dayname=='monday' or dayname=='sunday':
        checkbox.click()

#select last 2 checkbox
#range(10,12)
#total number of elements-2=starting element

for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()

#select first 2 checkbox

for i in range(len(checkboxes):
    if i<2:
     checkboxes[i].click()

#clearing all the checkboxes

for checkbox in checkboxes:
    if checkbox.is_selected():
    checkbox.click()

