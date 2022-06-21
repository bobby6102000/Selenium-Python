import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Firefox()

try:
    driver.get('https://formy-project.herokuapp.com/dragdrop')

    image = driver.find_element(By.ID,"image")

    box = driver.find_element(By.ID,'box')

    action = ActionChains(driver)

    action.drag_and_drop(source=image,target=box).perform()

    time.sleep(3)
finally:
    driver.quit()
