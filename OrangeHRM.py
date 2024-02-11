import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(5)
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"oxd-button").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
time.sleep(4)
#driver.find_element(By.LINK_TEXT,"Logout").click()
#driver.close()