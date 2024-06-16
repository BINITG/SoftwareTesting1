from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browserName="Chrome" #firefox/safari

if browserName == "Chrome":
    driver =webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
    driver=webdriver.Safari()
else:
    print("please pass the correct browser name:" + browserName)
    raise Exception('driver is not found')
driver.implicitly_wait(5)




import time

browserName="chrome"