import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#  relative X Path

#driver.get("https://m.facebook.com/")
#driver.find_element(By.XPATH, "//*[@id='m_login_email']").send_keys("Facebook user Name")
#driver.find_element(By.XPATH, "//*[@id='m_login_password']").send_keys("1234")

#X path absolute
#driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/form/div[4]/div[1]/div/div/input").send_keys("Facebook User Name")
#driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/form/div[4]/div[3]/div/div/div/div[1]/div/input").send_keys("1234")

#X path  and
#driver.find_element(By.XPATH,"//*[@id='m_login_email' and @name='email']"). send_keys("abc user name")

#X path or
#driver.find_element(By.XPATH,"//*[@id='m_login_email' or @name='mymail']"). send_keys("abc user name")

#X path contains()
#driver.find_element(By.XPATH,"//*[contains(@placeholder,'Mobile')]"). send_keys("abc user name")

#X path Start-wth()
#driver.find_element(By.XPATH,"//*[starts-with(@placeholder,'Mo')]"). send_keys("abc user name")

#X path Text

#driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

#driver.find_element(By.XPATH,"//*[text()='Log in']").click()
