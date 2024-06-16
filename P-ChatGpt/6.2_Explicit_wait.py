from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import  NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException

driver=webdriver.Chrome()
mywait=WebDriverWait(driver,10)#explicitwait declaration
mywait=WebDriverWait(driver,10,ignored_exceptions=[NoSuchElementException,
                                                   ElementNotVisibleException,
                                                   ElementNotSelectableException,
                                                   Exception]
                     )

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.XPATH,'//textarea[@name="q"]')
searchbox.send_keys("selenium")
searchbox.submit()

searchlink=mywait.until(EC.presence_of_element_located((BY.XPATH,"//h3[text()='selenium']")))
searchlink.click()

driver.quit()