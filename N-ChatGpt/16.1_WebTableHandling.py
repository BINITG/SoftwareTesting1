from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(15)

driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.maximize_window()

k=driver.find_element(By.XPATH,'//table[@id="customers"]/tbody/tr[3]/td[3]').text
print(k)

y=driver.find_element(By.XPATH,'//table[@id="customers"]/tbody/tr[7]/td[2]').text
print(y)

