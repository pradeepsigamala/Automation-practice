from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach", True)
service = Service(executable_path="C:\\Users\\prade\\OneDrive\\Documents\\chromedriver.exe")
driver=webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
numrows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
numcoum=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))


# for r in range(2,numrows+1):
#     for c in range(1,numcoum+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tbody/tr["+str(r)+"]//td["+str(c)+"]").text
#         print(data, end="       ")
#     print()

for r in range(2, numrows+1):
    auth_name = driver.find_element(By.XPATH,"//table[@name='BookTable']//tbody/tr["+str(r)+"]//td[2]").text
    if auth_name=="Amit":
        book = driver.find_element(By.XPATH,"//table[@name='BookTable']//tbody/tr["+str(r)+"]//td[1]").text
        price = driver.find_element(By.XPATH,"//table[@name='BookTable']//tbody/tr["+str(r)+"]//td[4]").text
        print(book,"       ",auth_name,"       ",price)
#

print(numrows)
print(numcoum)


# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.implicitly_wait(10)
# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME,"password").send_keys("admin123")
# driver.find_element(By.CLASS_NAME, "oxd-button").click()
#
# driver.find_element(By.LINK_TEXT,"Admin").click()
# driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
# driver.find_element(By.XPATH,"//ul[@role='menu']//li").click()
#
#
# numrows=driver.find_elements(By.XPATH, "(//div[@class='oxd-table-card'])/div/div[3]")
# numcolumn=driver.find_elements(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div")
#
# print(len(numrows))
# print(len(numcolumn))



# num = driver.find_elements(By.NAME,"oxd-table-header-cell oxd-padding-cell oxd-table-th")
# print(len(num))
# total=driver.find_elements(By.XPATH,"(//div[@class='oxd-table-card'])")
# print(len(total))
# numcolu=driver.find_element(By)
#
# for r in range
# table = driver.find_element(By.XPATH, "//div[@class='orangehrm-container']//div[2]//div["+str(r)+"]//div["+str(c)+"]").text
# print(table)




driver.close()