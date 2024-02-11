import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# 1 scroll down the page by pixel

driver.execute_script("window.scrollBy(0,3000)", "")
value = driver.execute_script("return window.pageYOffset;") #postition of the scroll
print("Number of pixels moved:", value) #3000

time.sleep(3)
# scroll till the element is visible
flag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value) #4974.39990234375

time.sleep(3)
# scroll till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value) # 6040

time.sleep(3)

#go back to start postion

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value) # 6040


time.sleep(3)
driver.close()
