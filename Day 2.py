from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

options=Options()
options.add_experimental_option("detach", True)
service = Service(executable_path="C:\\Users\\prade\\OneDrive\\Documents\\chromedriver.exe")
driver=webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)

# driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
# driver.maximize_window()
driver.get("https://www.youtube.com/")
driver.maximize_window()
driver.find_element(By.ID,"search").send_keys("Oggy")
driver.find_element(By.ID,"search").click()