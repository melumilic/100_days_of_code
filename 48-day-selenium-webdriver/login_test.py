from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(5)

driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name_field = driver.find_element(By.NAME, "fName")
l_name_field = driver.find_element(By.NAME, "lName")
f_email_field = driver.find_element(By.NAME, "email")
submit_button = driver.find_element(By.CSS_SELECTOR, "form button")
# submit_button = driver.find_element(By.XPATH, "/html/body/form/button")


fname = "j"
lname = "c"
email = "test@example.com"

f_name_field.send_keys(fname)
l_name_field.send_keys(lname)
f_email_field.send_keys(email)

submit_button.click()


