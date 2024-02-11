import links as links
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://demo.nopcommerce.com/")
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,"Digital downloads").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Digit").click()

driver.close()

# find number of links in a web page

# links=driver.find_elements(By.TAG_NAME, "a")
# print(total number of links = len(links))

links=driver.find_elements(By.XPATH,"//a")
print("total number of links=", len(links))
#
# #print all the links
#
# for link in links:
#     print(link.text)
# driver.close()