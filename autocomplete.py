import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

try:
    driver.get('https://formy-project.herokuapp.com/autocomplete')

    autocomplete = driver.find_element(By.ID,"autocomplete")
    autocomplete.click()
    autocomplete.send_keys("1555 Park Blvd, Palo Alto, CA")
    time.sleep(3)
    autocompleteResult = driver.find_element(By.CLASS_NAME,"dismissButton")
    autocompleteResult.click()

finally:
    driver.quit()
