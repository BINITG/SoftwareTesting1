from selenium import webdriver
from selenium.webdriver import ActionChains,DesiredCapabilities
from selenium.webdriver.chrome.options import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

#chrome:

#options=options()
#options.add_argument('--allow-running-insecure-content')
#options.add_argument('--ignore-certificate-errors')

#desired_capabilities=DesiredCapabilities().CHROME.copy()
#desired_capabilities['acceptInsecureCertificates']=True

options=options()
options.set_capability('acceptInsecureCerts',True)

driver=webdriver.Chrome(chrome_options=options)

driver.implicitly_wait(10)

driver=webdriver.Chrome()
driver.get("https://expired.badssl.com")

print(driver.find_element(By.TAG_NAME,'h1').text)