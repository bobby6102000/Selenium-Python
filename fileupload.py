from distutils import file_util
from re import I
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Firefox()

try:
    driver.get('https://formy-project.herokuapp.com/fileupload')

    fileUploadField = driver.find_element(By.ID,'file-upload-field')
    fileUploadField.send_keys('README.md')

    time.sleep(1)

finally:
    driver.quit()
