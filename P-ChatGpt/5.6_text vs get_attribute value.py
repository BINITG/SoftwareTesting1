from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
time.sleep(5)
email_box=driver.find_element(By.XPATH,'//input[@id="Email"]')

email_box.clear()
email_box.send_keys("abc@gmail.com")

print("result of text", email_box.text)
print("result of get_attribute()", email_box.get_attribute('value'))

button=driver.find_element(By.XPATH,'//button[@type="submit"]')
print("result of text::", button.text)
print("result of get_attribute()::", button.get_attribute('type'))