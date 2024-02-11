import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# windowid=driver.current_window_handle
# print(windowid)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowids=driver.window_handles

#Approach 1
# paremtwindow=windowids[0]
# childwindow=windowids[1]
#
# print(paremtwindow,childwindow)
#
# driver.switch_to(childwindow)
# print("Title of Child Window:",driver.title)
#
# driver.switch_to(paremtwindow)
# print("Title of Parent Window:",driver.title)

#Approach 2 (parent and child approach)
#
# for winid in windowids:
#     driver.switch_to.window(winid)
#     print(driver.title)

#Approach 3  (closing the windows based on our choice)

for winid in windowids:
    driver.switch_to.window(winid)
    if driver.title=="OrangeHRM": #(enter all the titles of the webpage which want to close)
        driver.close()





driver.close()