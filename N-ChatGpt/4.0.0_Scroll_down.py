from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()

import time
driver.implicitly_wait(15)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,1000)")
time.sleep(4)

flag=driver.find_element(By.XPATH,"//img[@src='flags-normal/flag-of-Bulgaria.png']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(4)






#METHOD-1=SCROLL DOWN  BY  PIXEL
#METHOD-2=SCROLL DOWN TILL PARTICULAR ELEMENT IS VISIBLE
#METHOD-3=SCROLL DOWN TILL END

