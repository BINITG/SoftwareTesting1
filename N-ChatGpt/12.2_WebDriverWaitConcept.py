from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver=webdriver.Chrome()

driver.get("https://app.hubspot.com/login")
driver.maximize_window()

wait=WebDriverWait(driver,10)                                    #MAX TIME IS 10S...SO IF ELEMENT CAN BE FOUND IN 5 SEC
wait.until(ec.title_is('Hubspot Login'))                         #EXPLICIT WAIT CONDITION-1
print(driver.title)

wait=WebDriverWait(driver,10)
email_id=wait.until(ec.presence_of_element_located((By.ID,"username")))    #EXPLICIT WAIT CONDITION-2
email_id.send_keys("test@gmail.com")

driver.find_element(By.ID,'password').send_keys('test@123')



#THERE IS SOME TIMEOUT ERROR...WILL SEE LATER