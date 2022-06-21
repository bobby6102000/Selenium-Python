import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Firefox()

try:
    driver.get('https://formy-project.herokuapp.com/checkbox')

    checkButton1 = driver.find_element(By.ID,'checkbox-1')
    checkButton1.click()
    time.sleep(1)
    
    checkButton2 = driver.find_element(By.CSS_SELECTOR,'input[value="checkbox-2"]')
    checkButton2.click()
    time.sleep(1)
    
    checkButton3 = driver.find_element(By.XPATH,'//*[@id="checkbox-3"]')
    checkButton3.click()

    time.sleep(1)

finally:
    driver.quit()
