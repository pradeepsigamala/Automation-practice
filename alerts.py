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

 #alerts case 1

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
alerts=driver.switch_to.alert
#alerts.send_keys("abc")
#alerts.accept()
print(alerts.text)
alerts.dismiss()




time.sleep(3)
driver.close()