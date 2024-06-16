from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Actionchains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#7 LINES CAN BE REMEMBERED AS ABOVE.

driver.find_element(By.XPATH,"")
driver.find_element(By.ID,"")
driver.find_element(By.NAME,"")
driver.find_element(By.CLASS_NAME,"")
driver.find_element(By.TAG_NAME,"")
driver.find_element(By.LINK_TEXT,"")
driver.find_element(By.PARTIAL_LINK_TEXT,"")
driver.find_element(By.CSS_SELECTOR,"")

driver=webdriver.Chrome()
import time
driver.implicitly_wait()
wait=WebDriverWait(driver,15)
ele=wait.until(ec.title_is('hubspot_login'))
ele=wait.until(ec.presence_of_element_located(''))
ele=wait.until(ec.new_window_is_opened(''))

driver.execute_script("window.scrollBy(0,300)")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.execute_script("arguments[0].scrollIntoView;",flag)

from selenium.webdriver.support.ui import Select
k=Select(driver.find_element(By.XPATH,"ID"))
k.select_by_index('9')
k.select_by_value('myanmar')
k.select_by_visible_text('india')

from selenium.webdriver import Actionchains
Actionchains(driver).move_to_element(element).perform()
Actionchains(driver).drag_and_drop(s,t).perform()
Actionchains(driver).context_click(element).perform()

driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
driver.switch_to.default_content()

driver.switch_to.frame(id)
driver.switch_to.frame(name)

driver.find_element(By.NAME,"UPLOAD BUTTON").send_keys(("file-location"))
driver.find_element(By.NAME,"submit-buttton").click()

driver.back()
driver.forward()
driver.refresh()

driver.get_cookies()
driver.add_cookie()

driver.get_screenshot_as_file('fname')
driver.save_screenshot('fname')

























