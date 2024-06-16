from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

searchbox=driver.find_element(By.XPATH,'//input[@id="small-searchterms"]')
print("Display status:",searchbox.is_displayed())
print("Enable status:",searchbox.is_enabled())

radio_button1=driver.find_element(By.XPATH,"//input[@id='gender-male']")
radio_button2=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("default radiobutton status")
print(radio_button1.is_selected())
print(radio_button2.is_selected())

radio_button1.click()
print("radio button status after selection of radiobutton1")
print(radio_button1.is_selected())
print(radio_button2.is_selected())

radio_button2.click()
print("radio button status after selection of radiobutton2")
print(radio_button1.is_selected())
print(radio_button2.is_selected())


driver.quit()