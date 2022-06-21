import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Firefox()

try:
    driver.get('https://formy-project.herokuapp.com/dropdown')

    DropDownMenu = driver.find_element(By.ID,'dropdownMenuButton')

    DropDownMenu.click()

    autocompleteItem = driver.find_element(By.ID,'autocomplete')
    autocompleteItem.click()


    time.sleep(1)

finally:
    driver.quit()
