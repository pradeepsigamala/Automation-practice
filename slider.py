from selenium import webdriver
from selenium.webdriver import ActionChains
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
driver.maximize_window()

slide = driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
print(slide.location)  #{'x': 980, 'y': 1372}

act = ActionChains(driver)
act.drag_and_drop_by_offset(slide, 100,0).perform()

print(slide.location)


