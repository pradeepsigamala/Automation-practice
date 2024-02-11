from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#chrome_options = Options()
options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

serv_obj=Service("E:\\New folder\\chromedriver.exe")
#driver=webdriver.Chrome(service=serv_obj, options=options)
#driver.get("https://www.google.co.in/")

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.ID,"RememberMe").click()
driver.find_element(By.CLASS_NAME,"login-button").click()
act_title= driver.title
exp_title="Dashboard / nopCommerce administration"
#exp_title="experiment"

if act_title==exp_title:
    print("Test is Passed")
else:
    print("Test is Failed")

driver.close()
