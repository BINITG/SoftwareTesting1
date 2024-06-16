from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
from selenium.webdriver.support.ui import Select

import time



def select_values(options_list,value):
    for ele in drop_list:
        print(ele.text)
        for k in range(len(value)):
            if ele.text==value[k]:
                ele.click()
                break


'''def select_values(options_list,value):
    for ele in drop_list:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break'''


driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element(By.ID,"justAnInputBox").click()

time.sleep(3)

drop_list=driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')
values_list=['choice 2','choice 3','choice 6 2 1']
select_values(drop_list,values_list)


'''drop_list=driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')
select_values(drop_list,'choice 2')
select_values(drop_list,'choice 3')
select_values(drop_list,'choice 6 2 1')'''


#for ele in drop_list:
#     print(ele.text)
#     if ele.text=='choice 2':
#         ele.click()
#        break













