#COUNT NO. OF ROWS & COLUMNS
#READ SPECIFIC ROW & COLUMN DATA
#READ ALL THE ROWS AND COLUMNS DATA
#READ DATA BASED  ON CONDITIONS(LIST BOOK NAME WHOSE AUTHOR IS MUKESH)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#COUNT NO. OF ROWS & COLUMNS

noofrows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
noofcolumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th"))

print(noofrows)
print(noofcolumns)

#READ SPECIFIC ROW & COLUMN DATA

data=driver.find_element(By.XPATH,'//table[@name="BookTable"]/tbody/tr[5]/td[1]').text
print(data)

#READ ALL THE ROWS AND COLUMNS DATA
#print("printing all the rows and cols data.....")

#for r in range(2,noofrows+1):
#   for c in range(1,noofcolumns+1):
#      data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#     print(data,end='  ')
#print()

#READ DATA BASED  ON CONDITIONS(LIST BOOK NAME WHOSE AUTHOR IS MUKESH)

for r in range(2,noofrows+1):
    authorname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorname=="Mukesh":
        bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookname,"    ",authorname,"    ",price)


