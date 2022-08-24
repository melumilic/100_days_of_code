from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(5)

browser.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = browser.find_element(By.ID,"cookie")

cookie_count = browser.find_element(By.ID,"money")

# shops
cursor = browser.find_element(By.ID,"buyCursor")
grandma = browser.find_element(By.ID,"buyGrandma")
factory = browser.find_element(By.ID,"buyFactory")
mine= browser.find_element(By.ID,"buyMine")
shipment = browser.find_element(By.ID,"buyShipment")
alchemy_lab = browser.find_element(By.ID,"buyAlchemy lab")
portal = browser.find_element(By.ID,"buyPortal")
time_machine = browser.find_element(By.ID,"buyTime machine")

buy_delay = 10
t_end = time.time() + 60 * 1
t_buy = time.time() + buy_delay
while time.time() < t_end:
    cookie.click()
    if time.time() >= t_buy:
        while int(browser.find_element(By.ID,"money").text)>=19:
            if int(browser.find_element(By.ID,"money").text) >=123456789:
                time_machine.click()
            elif int(browser.find_element(By.ID,"money").text) >=1000000:
                portal.click()
            elif int(browser.find_element(By.ID,"money").text) >=50000:
                alchemy_lab.click()
            elif int(browser.find_element(By.ID,"money").text) >=7000:
                shipment.click()
            elif int(browser.find_element(By.ID,"money").text) >=2000:
                mine.click()
            elif int(browser.find_element(By.ID,"money").text) >=500:
                factory.click()
            elif int(browser.find_element(By.ID,"money").text) >=100:
                grandma.click()
            elif int(browser.find_element(By.ID,"money").text) >=19:
                cursor.click()
        t_buy = time.time() + buy_delay

print(browser.find_element(By.ID,"cps").text)
browser.quit()