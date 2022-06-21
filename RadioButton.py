import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Firefox()

try:
    driver.get('https://formy-project.herokuapp.com/radiobutton')

    radioButton1 = driver.find_element(By.ID,'radio-button-1')
    radioButton1.click()
    time.sleep(1)
    
    radioButton2 = driver.find_element(By.CSS_SELECTOR,'input[value="option2"]')
    radioButton2.click()
    time.sleep(1)
    
    radioButton3 = driver.find_element(By.XPATH,"/html/body/div/div[3]/input")
    radioButton3.click()

    time.sleep(1)

finally:
    driver.quit()
