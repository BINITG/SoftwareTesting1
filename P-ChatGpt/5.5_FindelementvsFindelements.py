from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

######find_element()- returns single webelement

#1.locator matching with single web element
#element=driver.find_element(By.XPATH,'//input[@id="small-searchterms"]')
#element.send_keys("acer laptop")

#2.locator matching with multiple web elements
#elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
#print(elements.text)

#3.element not available then throw nosuch element exception
#loginelement=driver.find_element(By.LINK_TEXT,"Log")
#loginelement.click()

######find_elements()- Returns multiple webelements

#1.locator matching with single web element
#elements=driver.find_elements(By.XPATH,'//input[@id="small-searchterms"]')
#print(len(elements))
#elements [0].send_keys("apple mac book")
#time.sleep(5)

#2.locator matching with multiple web elements
#elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
#print(len(elements))
#print(elements[0].text)# to print first element from list

#for ele in elements:
#    print(ele.text)# to print all matching elements

#3.element not available
loginelement=driver.find_elements(By.LINK_TEXT,"Log")
print("elements returned:",len(loginelement))