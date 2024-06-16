from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
import time
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
time.sleep(3)

#DATE OF BIRTH

driver.find_element(By.XPATH,"//input[@id='dob']").click()

datepicker_month=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
datepicker_month.select_by_visible_text("Dec") #MONTH

datepicker_year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectyear']"))
datepicker_year.select_by_visible_text("1990")

alldates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a ")

for date in alldates:
    if date.text=="25":
        date.click()
        break
time.sleep(5)


