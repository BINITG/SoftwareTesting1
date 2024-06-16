from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

import time
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.maximize_window()

source=driver.find_element(By.ID,'draggable')
target=driver.find_element(By.ID,'droppable')

ActionChains(driver).drag_and_drop(source,target).perform()
ActionChains(driver).click_and_hold(source).move_to_element(target).release().perform()
time.sleep(5)