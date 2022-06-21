from selenium import webdriver
#import to get the elements by different attributes
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

try:
    driver.get('http://the-internet.herokuapp.com/login')
    
    user = driver.find_element(By.ID,'username')
    password = driver.find_element(By.ID,'password')
    submit = driver.find_element(By.CSS_SELECTOR,'button[type=submit]')

    #.send keys method is used for passing the text in the attribute
    user.send_keys('tomsmith')
    password.send_keys('SuperSecretPassword!')
    submit.click()
    afterlogin = driver.find_element(By.ID,'flash').text

    if ('You logged into a secure area!' in afterlogin):
        print("Logged in successful")
    
finally:
    driver.quit()
