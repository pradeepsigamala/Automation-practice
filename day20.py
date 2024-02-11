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

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.implicitly_wait(3)
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.implicitly_wait(3)
driver.find_element(By.CLASS_NAME,"oxd-button").click()

admin=driver.find_element(By.XPATH,"//a[normalize-space()='']")
usermanage=driver.find_element(By.XPATH,"//span[normalize-space()='User Management']")
user=driver.find_element(By.XPATH,"//a[normalize-space()='Users']")

act=ActionChains(driver)
act.move_to_element(admin).move_to_element(usermanage).move_to_element(user).click()
time.sleep(3)
driver.close()
