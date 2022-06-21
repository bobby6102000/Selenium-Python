from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

try:
    driver.get('https://formy-project.herokuapp.com/keypress')

    name = driver.find_element(By.ID,'name')
    name.click()
    name.send_keys('Bhavin')

    button = driver.find_element(By.ID,"button")
    button.click()

finally:
    driver.quit()
