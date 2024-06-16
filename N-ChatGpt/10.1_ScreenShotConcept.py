from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.implicitly_wait(10)
import time

driver.get("https://www.reddit.com/")
driver.maximize_window()

#driver.get_screenshot_as_file('reddit.png')    #METHOD-1 TO TAKE SCREENSHOT
driver.save_screenshot('Binit.jpeg')            #METHOD-2 TO TAKE SCREESHOT












#full screenshot'''----'''Make sure that you are running in headless mode'''

'''s=lambda X:driver.execute_script('return document.body.parentNode.scroll'+X)      #USING JAVA CODE
driver.set_window_size(s('width'),s('height'))
driver.find_element_by_tag_name('body').screenshot('reddit_full.png')'''


#FOR FULL SCREEN SHOT ,HEADLESS MODE IS MANDATORY.SO I AM FACING ISSUE IJ HEADLESSS MODE COCEPT.
