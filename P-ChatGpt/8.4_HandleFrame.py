from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")#not working frame url
driver.maximize_window()

driver.switch_to.frame("packageListFFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content() #GO BACK TO MAIN PAGE

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"webDriver").click()
driver.switch_to.default_content() #GO BACK TO MAIN PAGE

driver.switch_to.frame("classFrame")
driver.find_element(By.LINK_TEXT,"/html/body/header/nav/div[1]/div[1]/ul/li[[8]").click()























