from selenium import webdriver
# Remote webdriver Server
caps = {
    'browserName': 'firefox'
}

driver = webdriver.Remote(
    command_executor=  'http://127.0.0.1:4444',
    desired_capabilities=caps
)

driver.quit()