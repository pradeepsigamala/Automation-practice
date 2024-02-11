#we need to install request package through, file>settings>project interpretter>requests
import requests
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

driver.get("http://www.deadlinkcity.com/")
links =driver.find_elements(By.TAG_NAME,"a")

count=0
for link in links:
    url=link.get_attribute("href")
    try:
         resp= requests.head(url)
    except:
        None

    if resp.status_code>=400:
        print(url, "link is broken")
        count+=1
    else:
       print(url, "link is valid")

print("total number of links=",count)


driver.close()