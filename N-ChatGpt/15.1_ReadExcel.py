
from selenium import webdriver
from selenium.webdriver.common.by import By

import xlrd

driver=webdriver.Chrome()
import time


driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

workbook=xlrd.open_workbook("DataFile.xlsx")
sheet=workbook.sheet_by_name("login")

#get total number of rows:
rowCount=sheet.nrows
colCount=sheet.ncols
ptint(rowCount)
print(colCount)

for curr_row in range(1,rowCount):
    username=sheet.cell_value(curr_row,0)
    password=sheet.cell_value(curr_row,1)

    print(user_name + " " + password)
