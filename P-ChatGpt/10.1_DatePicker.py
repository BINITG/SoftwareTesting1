from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
time.sleep(3)

driver.switch_to.frame(0)

#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/03/2022 ")
time.sleep(3)

year="2024"
month="aug"
date="30"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break
    else:
        driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[2]/span').click() #NEXT ARROW
        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[1]/span').click()  #PREVIOUS ARROW-OLD DATE

#SELECT DATE

dates=driver.find_elements(By.XPATH,'//div[@id="ui-datepicker-div"]//table/tbody/tr/td/a')

for ele in dates:
    if ele.text==date:
        ele.click()
        break
