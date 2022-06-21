from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

try:
    driver.get('https://formy-project.herokuapp.com/switch-window')

    alertButton = driver.find_element(By.ID,'alert-button')
    alertButton.click()

    #switch to is used for focousing toalert and alerts accept is used to click ok button 
    driver.switch_to.alert.accept()

finally:
    driver.quit()
