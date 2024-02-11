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
driver.implicitly_wait(10)
# driver.find_element(By.CLASS_NAME,"btn").click()

drpdn_ele=driver.find_element(By.XPATH,"//select[@class='custom-select']")
drpdn=Select(drpdn_ele)

#drpdn.select_by_visible_text("Italy")
drpdn.select_by_value("5")
#drpdn.select_by_index(2)


allopt=drpdn.options
print("Totla number of Options:",len(allopt))

for opt in allopt:
    print(opt.text)






time.sleep(3)

driver.close()


