import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

try:
    driver.get('https://formy-project.herokuapp.com/datepicker')

    dateField = driver.find_element(By.ID,'datepicker')
    dateField.send_keys(11/11/2021)
    dateField.send_keys(Keys.ENTER)
    time.sleep(2) 

finally:
    driver.quit()
