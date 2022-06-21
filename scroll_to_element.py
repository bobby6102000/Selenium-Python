from argparse import Action
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

try:
    driver.get('https://formy-project.herokuapp.com/scroll')

    name = driver.find_element(By.ID,"name")
    # import AcrtionChains to implement scrolls 
    action = webdriver.ActionChains(driver)
    # move to elememts are used for scroll to the element
    action.move_to_element(name)
    name.send_keys("Bhavin Patel")

    date = driver.find_element(By.ID,'date')
    date.send_keys("11/11/2021")

    time.sleep(2)
    
   
finally:
    driver.quit()
