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

driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.ID,"datepicker").click()
# driver.implicitly_wait(10)

year = "2025"
month = "January"
date = "15"

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon==month and yr==year:
            break;
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody//a")

for ele in dates:
    if ele.text==date:
        ele.click()
driver.close()


