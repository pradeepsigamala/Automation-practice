from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Ctrl+A
# Ctrl+C
# Tab
# Ctrl+V

driver.get("https://text-compare.com/")
box1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
box2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

box1.send_keys("welcome to page")

act=ActionChains(driver)

