import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

def formfill():
    driver.get('https://formy-project.herokuapp.com/form')

    driver.find_element(By.ID,'first-name').send_keys("Bhavin")

    driver.find_element(By.ID,'last-name').send_keys("patel")

    driver.find_element(By.ID,'job-title').send_keys("Software Tester")

    driver.find_element(By.ID,'radio-button-2').click()

    driver.find_element(By.ID,'checkbox-2').click()

    driver.find_element(By.CSS_SELECTOR,'option[value="2"]').click()

    driver.find_element(By.ID,'datepicker').send_keys("11/11/2020")

    driver.find_element(By.ID,'datepicker').send_keys(Keys.RETURN)

    driver.find_element(By.CSS_SELECTOR,'.btn.btn-lg.btn-primary').click()
 

try:
    formfill()
    
    alert = driver.find_element(By.CLASS_NAME,"alert").text

    if 'The form was successfully submitted!' in alert:
        print('Form Submitted')
    
    time.sleep(2)

finally:
    driver.quit()
