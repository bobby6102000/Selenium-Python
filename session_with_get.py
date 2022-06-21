from selenium import webdriver

driver = webdriver.Firefox()

'''
implement try and finally block 
so that the quit is always execute
to clean up the system resources
'''

try:
    driver.get('http://the-internet.herokuapp.com')
finally:
    driver.quit()
