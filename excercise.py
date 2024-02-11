import time
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

# for week in checkboxes:
#     weekname= week.get_attribute('id')
#     if weekname== 'monday' or weekname== 'saturday' or weekname=='sunday':
#      week.click()


for week in checkboxes:
    weekname= week.get_attribute('id')
    if weekname== 'monday' or weekname== 'saturday' or weekname=='sunday':
     week.click()
time.sleep(2)

for week in checkboxes:
    # if week.is_selected():
         week.click()


time.sleep(3)
driver.close()
