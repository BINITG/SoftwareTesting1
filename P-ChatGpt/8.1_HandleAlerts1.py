from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#OPEN ALERT WINDOW
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(5)

alertwindow=driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("welcome")

#alertwindow.accept()#CLOSE ALERT WINDOW USING OK BUTTON
alertwindow.dismiss()
time.sleep(3)