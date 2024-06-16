from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

#LOGIN
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]').click()
time.sleep(3)

#Admin-->usermanagement-->users
driver.find_element(By.XPATH,"//span[text()='Admin']")
driver.find_element(By.XPATH,"//span[text()='User Management ']")
driver.find_element(By.XPATH,"//ul[@class='oxd-dropdown-menu']//li")

#total no of rows in a table
rows=len(driver.find_element(By.XPATH,"//table[@id='resultTable']//tbody/tr"))
print("total no of rows in a table:",rows)

count=0
for r in range(1,rows+1):
    status=driver.find_element(By.XPATH,"//table[@id='resultTable']//tbody/tr["+str(r)+"]/td[5]").text
    if status=="Enabled":
        count=count+1

print("Total no of users:",count)
print("Number of enabled users:",count)
print("Number of disabled users:",(rows-count))

driver.close()















