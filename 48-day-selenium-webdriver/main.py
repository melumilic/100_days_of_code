from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from pprint import pprint

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(5)

# driver.get(
#     "https://brevite.co/products/the-brevite-backpack?variant=34952238858394&=undefined"
# )
# price = driver.find_element(By.CLASS_NAME, "money")
# print(price.text)

# form_field = driver.find_element(By.NAME,"")

# ccs_example = driver.find_element(By.CSS_SELECTOR, ".class a h3 span div.classname")

driver.get("https://python.org")

event_dates = driver.find_elements(By.CSS_SELECTOR,"div.event-widget div ul.menu li time")
event_names = driver.find_elements(By.CSS_SELECTOR,"div.event-widget div ul.menu li a")

event_dict = [{time.text:name.text} for time,name in zip(event_dates,event_names)]
pprint(event_dict)

# this just lets you have the mouse click in one call instead of doing click() on a selenium driver object
# all_portals = driver.find_element_by_link_text("All portals")

from selenium.webdriver.common.keys import Keys
search = driver.find_element(By.NAME,"search")
search.send_keys("string you want to enter into the textfield")
search.send_keys(Keys.ENTER)

# driver.close()
driver.quit()
