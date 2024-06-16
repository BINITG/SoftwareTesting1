from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.implicitly_wait(15)
url="https://www.flipkart.com/"
driver.get(url)
driver.maximize_window()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
driver.find_element(By.XPATH,"//span[text()='Sign in']").click()
#driver.find_element(By.XPATH,'//input[@class="_2IX_2- VJZDxU"]').send_keys('7979024390')
#driver.find_element(By.XPATH,"//span[text()='Electronics']").click()
