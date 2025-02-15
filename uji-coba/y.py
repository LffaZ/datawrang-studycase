from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv

chrome_options = Options()
service = Service(executable_path="chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(f'https://en.wikipedia.org/wiki/Sukarno')

wait = WebDriverWait(driver, 10)

def sps():
    spouses = []
    spouses_name = driver.find_elements(By.XPATH, "//div[@class='marriage-display-ws']")

    for sps in spouses_name:
        name = sps.find_element(By.XPATH, ".//div[1]").text
        if sps.find_elements(By.XPATH, ".//abbr[@title='divorced']"):
            name = f"{name} (Cerai)"

        spouses.append(name)
    print(spouses)

def child():
    child_name = driver.find_element(By.XPATH, "//th[text()='Children']/following-sibling::td").text
    print(child_name)

parent = []
parent_name = driver.find_elements(By.XPATH, "//th[text()='Parents']/following-sibling::td/div/ul/li")
for name in parent_name:
    if name.text != '': parent.append(name.text)
print(parent)

driver.quit()

