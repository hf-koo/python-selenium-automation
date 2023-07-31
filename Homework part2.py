from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path='/Users/ahdoy/Desktop/QA/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# click on Account button
driver.find_element(By.ID, "nav-link-accountList").click()

sleep(3)

another_text = driver.find_element(By.XPATH, "//i[@aria-label='Amazon']").text
print(another_text)

sleep(3)

assert "Sign in" in driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

# header = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
# print(header)

print('Test Passed')
