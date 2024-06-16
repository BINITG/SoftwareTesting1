from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()

import time
driver.implicitly_wait(10)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.maximize_window()

#def select_values(element,value):
    #select=Select(element)
    #select.select_by_visible_text(value)

def select_values_from_dropdown(dropDownOptionsList,value):
    print(len(dropDownOptionsList))
    for ele in dropDownOptionsList:
        print(ele.text)
        if ele.text==value:
            ele.click()
            break

countri_list=driver.find_elements(By.XPATH,'//select[@required="required"]/option')
select_values_from_dropdown(countri_list,'Bangladesh')
select_values_from_dropdown(countri_list,'Angola')
time.sleep(5)




#ele_indus=driver.find_element(By.ID,'Form_submitForm_Industry')
#ele_country=driver.find_element(By.ID,"Form_getForm_Country")

#select_values(ele_indus,'Education')
#select_values(ele_Country,'India')

#ele_country=driver.find_element(By.ID,"Form_getForm_Country")
#select=Select(ele_country)

#select.select_by_visible_text("Bangladesh")
#select.select_by_index(4)
#select.select_by_value("Azerbaijan")

#print(select.is_multiple)

#select=Select(ele_country)
#coun_list=select.options

#for ele in coun_list:
#    print(ele.text)
#    if(ele.text=='Bangladesh'):
#        ele.click()
#        break

countri_list=driver.find_elements(By.XPATH,'//select[@required="required"]/option')
print(len(countri_list))
for ele in countri_list:
    print(ele.text)
    if ele.text=='Bangladesh':
        ele.click()
        break












