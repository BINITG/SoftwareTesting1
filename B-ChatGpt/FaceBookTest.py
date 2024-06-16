from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.google.com/')
ele = driver.find_element(By.NAME, 'q')
ele.send_keys('facebook')
ele.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, "//h3[text()='Facebook - log in or sign up']").click()
assert driver.page_source.find("Facebook")
assert driver.page_source.find("Facebook helps you connect and share with the people in your life.")
text = driver.find_element(By.XPATH,"//h2[text() ='Facebook helps you connect and share with the people in your life.']").text
print(text)
time.sleep(3)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys('8386973745')
driver.find_element(By.XPATH, '//input[@id="pass"]').send_keys('vikky8386')
driver.find_element(By.XPATH, '//button[@name="login"]').click()
time.sleep(5)
