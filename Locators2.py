import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://m.facebook.com/")

#Tag & ID
#driver.find_element(By.CSS_SELECTOR, "input#m_login_email").send_keys("my user name")
#driver.find_element(By.CSS_SELECTOR, "#m_login_email").send_keys("my user name")

#Tag & Class
#driver.find_element(By.CSS_SELECTOR, "input._56bg").send_keys("other user name")
#driver.find_element(By.CSS_SELECTOR, "._56bg _4u9z _5ruq _8qtn").send_keys("other user name")

#Tag & Attribute
#driver.find_element(By.CSS_SELECTOR, "input[type=text]").send_keys("new user name")
#driver.find_element(By.CSS_SELECTOR, "[type=text]").send_keys("new user name")

#Tag & class & attribute

#driver.find_element(By.CSS_SELECTOR, "input._56bg[placeholder=Password]").send_keys("created user name")
#driver.find_element(By.CSS_SELECTOR, "._56bg[placeholder=Password]").send_keys("created user name")

time.sleep(2)

driver.close()
