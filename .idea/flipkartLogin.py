from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.flipkart.com/')
driver.find_element(By.XPATH,'//input[@class="_2IX_2- VJZDxU"]').send_keys('7979024390')
driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _2HKlqd _3AWRsL"]').click()
#driver.find_element(By.XPATH,'//body[@class="fk-modal-visible"]').send_keys('635497')