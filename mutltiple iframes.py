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
driver.maximize_window()

driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()

outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

# innerframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
innerframe=driver.find_element(By.XPATH,"/html[1]/body[1]/section[1]/div[1]/div[1]/iframe[1]")

driver.switch_to.frame(innerframe)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome")

time.sleep(3)
driver.close()

