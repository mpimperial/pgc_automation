import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
#chrome_options.add_argument("headless") -- run the codes without the GUI

driver = webdriver.Chrome()
driver.get("https://web.uat.ucms.palawanpawnshop.com/business/#/login")
driver.maximize_window()

# Log in to the website
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("adminuser")
driver.find_element(By.ID, "password").send_keys("Admin@123")
driver.find_element(By.CLASS_NAME, "form-check-label").click()
driver.find_element(By.CSS_SELECTOR, "button[ng-click='accept()']").click()
driver.find_element(By.ID, "businessLogin").click()

time.sleep(5)