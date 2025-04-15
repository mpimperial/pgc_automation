import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("headless") --Run the test without GUI

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://web.uat.ucms.palawanpawnshop.com/business/#/login")

def clear_form():
    fields = ["First Name", "Last Name", "Date Of Birth", "SUKI Card No.", "Customer ID No."]
    for field in fields:
        driver.find_element(By.XPATH, f"//input[@placeholder='{field}']").clear()

def click_apply_button():
    driver.find_element(By.XPATH, "//button[@title='Search Apply']").click()

def click_customer_module():
    driver.find_element(By.CSS_SELECTOR, ".nav-link[ui-sref='accountDetails']").click()


# Log in to the website
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("marmar")
driver.find_element(By.ID, "password").send_keys("Imperi@l123")
driver.find_element(By.CLASS_NAME, "form-check-label").click()
driver.find_element(By.CSS_SELECTOR, "button[ng-click='accept()']").click()
driver.find_element(By.ID, "businessLogin").click()

# Select the business Branch
dropdown_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "firstDropdown_value")))
dropdown_input.send_keys("zzz-head office")

options = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class, 'angucomplete-row')]")))
for item in options:
    if item.text.strip().lower() == "zzz-head office":  # Case-insensitive comparison
        item.click()
        break
driver.find_element(By.CSS_SELECTOR, "button[ng-click='saveAndProceed(selectedBusiness)']").click()

# Fill out the form with data
driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("marwin")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("imperial")
date_of_birth = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Date Of Birth']"))
)
date_of_birth.send_keys("10/17/2000")
driver.find_element(By.XPATH, "//input[@placeholder='SUKI Card No.']").send_keys("qwerty")
driver.find_element(By.XPATH, "//input[@placeholder='Customer ID No.']").send_keys("zzz0425144491916")
click_apply_button()

# Extracting the displayed results
wait = WebDriverWait(driver, 15)
displayed_first_name = wait.until(EC.presence_of_element_located((By.XPATH, "//td[.//span[@title='MARWIN']]"))).text
displayed_last_name = wait.until(EC.presence_of_element_located((By.XPATH, "//td[.//span[@title='IMPERIAL']]"))).text
displayed_date_of_birth = wait.until(EC.presence_of_element_located((By.XPATH, "//td[.//span[@title='10/17/2000']]"))).text
displayed_suki_card = wait.until(EC.presence_of_element_located((By.XPATH, "//td[.//span[@title='QWERTY']]"))).text
displayed_customer_id = wait.until(EC.presence_of_element_located((By.XPATH, "//td[.//span[@title='ZZZ0425144491916']]"))).text

# Validation if the inputted data is equal to the displayed data
inputted_firstname = driver.find_element(By.XPATH, "//input[@placeholder='First Name']").get_attribute("value")
assert displayed_first_name.lower() in inputted_firstname, f"Assertion failed: {displayed_first_name} != {inputted_firstname}"
print("The inputted first name matches the displayed first name.")
inputted_lastname = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").get_attribute("value")
assert displayed_last_name.lower() in inputted_lastname.lower(), f"Assertion failed: {displayed_last_name} != {inputted_lastname}"
print("The inputted last name matches the displayed last name.")
inputted_date_of_birth = date_of_birth.get_attribute("value")
assert displayed_date_of_birth in inputted_date_of_birth, f"Assertion failed: {displayed_date_of_birth} != {displayed_date_of_birth}"
print("The inputted date of birth matches the displayed date of birth")
inputted_suki_card = driver.find_element(By.XPATH, "//input[@placeholder='SUKI Card No.']").get_attribute("value")
assert displayed_suki_card.lower() in inputted_suki_card, f"Assertion failed: {displayed_suki_card} != {inputted_suki_card}"
print("The inputted SUKI Card No. matches the displayed SUKI Card No.")
inputted_customer_id = driver.find_element(By.XPATH, "//input[@placeholder='Customer ID No.']").get_attribute("value")
assert displayed_customer_id.lower() in inputted_customer_id, f"Assertion failed: {displayed_customer_id} != {inputted_customer_id}"
print("The inputted Customer ID No. matches the displayed Customer ID No.")

clear_form()
driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("marwin")
click_apply_button()
time.sleep(1)
click_customer_module()

clear_form()
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("imperial")
click_apply_button()
time.sleep(1)
click_customer_module()

clear_form()
wait = WebDriverWait(driver, 10)

date_of_birth = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Date Of Birth']"))
)
date_of_birth.send_keys("10/17/2000")
click_apply_button()
time.sleep(1)
click_customer_module()

clear_form()
driver.find_element(By.XPATH, "//input[@placeholder='SUKI Card No.']").send_keys("qwerty")
click_apply_button()
time.sleep(1)
click_customer_module()

clear_form()
driver.find_element(By.XPATH, "//input[@placeholder='Customer ID No.']").send_keys("zzz0425144491916")
click_apply_button()
time.sleep(1)
click_customer_module()
# Wait for any action

time.sleep(5)
