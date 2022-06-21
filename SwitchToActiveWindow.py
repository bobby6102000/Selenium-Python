from netrc import netrc
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

try:
    driver.get('https://formy-project.herokuapp.com/switch-window')

    newTabButton = driver.find_element(By.ID,"new-tab-button")
    newTabButton.click()
    #get the windowhandler for the original page
    originalHandle=driver.current_window_handle
    
    #iterate throughs the windows
    for handle1 in driver.window_handles:
        driver.switch_to.window(handle1)
    
    driver.switch_to.window(originalHandle)

finally:
    driver.quit()
