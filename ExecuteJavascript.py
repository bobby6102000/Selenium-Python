import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

try:
    driver.get('https://formy-project.herokuapp.com/modal')

    modalButton = driver.find_element(By.ID,"modal-button")
    modalButton.click()

    closeButton = driver.find_element(By.ID,"close-button")
    #it is used to execute the javascript into the script
    driver.execute_script("arguments[0].click();",closeButton)
finally:
    driver.quit()
