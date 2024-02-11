import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach", True)
service = Service(executable_path="C:\\Users\\prade\\OneDrive\\Documents\\chromedriver.exe")
driver=webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)


driver.get("https://itera-qa.azurewebsites.net/home/automation")
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id, 'day')]")
print(len(checkboxes))

# approach 1 for loop

# for i in range(len(checkboxes)):
#     checkboxes[i].click()
#checkboxes[i].click()


# approach 2
#
for checkbox in checkboxes:
    checkbox.click()

#
# time.sleep(5)
# checkbox.click()

# approch 3

# for checkbox in checkboxes:
#
#     weekname=checkbox.get_attribute('id')
#
#     if weekname=='monday' or weekname =='wednesday' or weekname== 'sunday':
#      checkbox.click()
#

#approach 4

# for i in range (len(checkboxes)-2,len(checkboxes)):
#         checkboxes[i].click()

# for i in range (len(checkboxes)):
#         if i<2:
#          checkboxes[i].click()


# clearing all the check box
time.sleep(3)
for checkbox in checkboxes:
        if checkbox.is_selected():

         checkbox.click()


time.sleep(3)
# driver.close()


