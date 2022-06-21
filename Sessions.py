# import selenium driver
from selenium import webdriver

#Set the webdriver to use the firefox and starts the session
driver = webdriver.Firefox()

# Closes the session
driver.quit()
