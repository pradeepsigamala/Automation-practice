import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach", True)
# options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")


## practice 1
# driver.find_element(By.XPATH,"//button[normalize-space()='Click Me']").click()
# alert=driver.switch_to.alert
# alert.accept()
# # alert.dismiss()
#
#
# driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium")
# driver.find_element(By.XPATH,"//input[@type='submit']").click()
#
# links=driver.find_elements(By.ID,"wikipedia-search-result-link")
# print(len(links))
#
# for link in links:
#     print(link.text)
#
# driver.find_element(By.LINK_TEXT,"Selenium").click()
# driver.find_element(By.LINK_TEXT,"Selenium in biology").click()
# driver.find_element(By.LINK_TEXT,"Selenium (software)").click()
# driver.find_element(By.LINK_TEXT,"Selenium disulfide").click()
# driver.find_element(By.LINK_TEXT,"Selenium deficiency").click()
#
#
# windowids=driver.window_handles
#
# for winid in windowids:
#     driver.switch_to.window(winid)
#     print(driver.title)
#
#     # if driver.title == "Selenium - Wikipedia" or driver.title== "Selenium disulfide - Wikipedia":
#     #     driver.close()

#practice 2

driver.switch_to.frame("frame-one1434677811")

driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Chinni")
driver.find_element(By.ID,"RESULT_TextField-2").send_keys("Deepu")
driver.find_element(By.ID,"RESULT_TextField-3").send_keys("1234567890")
driver.find_element(By.ID,"RESULT_TextField-4").send_keys("India")
driver.find_element(By.ID,"RESULT_TextField-5").send_keys("kadapa")
driver.find_element(By.ID,"RESULT_TextField-6").send_keys("abc@gmail.com")


driver.find_element(By.XPATH,"//iframe[@id='frame-one1434677811']").click()

driver.find_element(By.XPATH,"(//iframe[@id='frame-one1434677811'])[1]").submit()
##practice once
# weeks=driver.find_elements(By.CLASS_NAME,"multiple_choice")
# print(len(weeks))
#
# for week in weeks:
#      week.click()
#      print(week.text)
#
#
# # time.sleep(3)
driver.quit()