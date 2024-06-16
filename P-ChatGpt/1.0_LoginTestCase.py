from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]').click()
actual_title=driver.title
expected_title="OrangeHRM"
if actual_title==expected_title:
    print("test passed")
else:
    print("test failed")
driver.close()

