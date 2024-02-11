from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

item1 = driver.find_element(By.XPATH,"//li[1]")
item2 = driver.find_element(By.XPATH,"//img[@alt='the peaks of high tatras']")
target = driver.find_element(By.XPATH,"//div[@id='trash']")
act = ActionChains(driver)

act.drag_and_drop(item1, target).perform()
act.drag_and_drop(item2, target).perform()

sorce = driver.find_element(By.XPATH,"//div[@id='draggable']")
target = driver.find_element(By.XPATH,"//div[@id='droppable']")

act.drag_and_drop(sorce, target).perform()