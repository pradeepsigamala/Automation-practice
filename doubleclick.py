import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
field = driver.find_element(By.XPATH,"//input[@id='field1']")
field.clear()
field.send_keys("senior")

button = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
act = ActionChains(driver)
act.double_click(button).perform()




# driver.close()