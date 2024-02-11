import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

serv_obj=Service("E:\\New folder\\chromedriver.exe")
driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-1878168699%3A1677347435487482&authuser=0&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgamil%26oq%3Dgamil%26aqs%3Dchrome..69i57j0i10i131i433i512l3j0i10i433i512l2j0i10i131i433i512l2j0i10i433i512j0i10i512.1966j0j7%26sourceid%3Dchrome%26ie%3DUTF-8&ec=GAlAAQ&hl=en&flowName=GlifWebSignIn&flowEntry=AddSession")
time.sleep(5)
driver.find_element(By.ID,"identifierId").send_keys("teju.rvd@gmail.com")
time.sleep(15)
#driver.find_element(By.CLASS_NAME, "VfPpkd-RLmnJb").click()