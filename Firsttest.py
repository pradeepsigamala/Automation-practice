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

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME, "username").send_keys("Admin")
#driver.find_element(By.NAME,"password").send_keys("admin123")
#driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()