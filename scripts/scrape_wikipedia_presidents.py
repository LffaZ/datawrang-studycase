from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv

chrome_options = Options()
service = Service(executable_path="driver/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

listPres = 'https://en.wikipedia.org/wiki/List_of_presidents_of_Indonesia'

driver.maximize_window()
driver.get(listPres)

wait = WebDriverWait(driver, 10)

features = ['nama', 'tgl_lahir', 'masa_jab', 'nama_si', 'nama_anak', 'nama_ortu']
president_data = []

def spouse():
    spouses = []
    spouses_name = driver.find_elements(By.XPATH, "//div[@class='marriage-display-ws']")

    for sps in spouses_name:
        name = sps.find_element(By.XPATH, ".//div[1]").text
        if sps.find_elements(By.XPATH, ".//abbr[@title='divorced']"):
            name = f"{name} (Cerai)"

        spouses.append(name)

    return spouses

def child():
    child_name = driver.find_element(By.XPATH, "//th[text()='Children']/following-sibling::td").text
    return child_name

def parent():
    parent = []
    parent_name = driver.find_elements(By.XPATH, "//th[text()='Parents']/following-sibling::td/div/ul/li")
    for name in parent_name:
        if name.text != '': parent.append(name.text)

    return parent

def fam(name):
    driver.get(f'https://en.wikipedia.org/wiki/{name.replace(" ", "_")}')

    image_url = driver.find_element(By.XPATH, "//td[@class='infobox-image']/span/a/img").get_attribute("src")

    for data in president_data:
        if data['name'] == name:
            data['spouse'] = spouse()
            data['child'] = child()
            data['parent'] = parent()
            data['img'] = image_url

rows = driver.find_elements(By.XPATH, "//tr[@style='text-align: left; background:#FFFFFF']")
for row in rows:
    name = row.find_element(By.XPATH, ".//td[2]/a").text
    birth_date = row.find_element(By.XPATH, ".//td[3]/span").text
    start_date = row.find_element(By.XPATH, ".//td[4]/span[2]").text
    try:
        end_date = row.find_element(By.XPATH, ".//td[5]/span[2]").text
    except Exception:
        end_date = 'sekarang'

    print(f"Nama: {name}")
    print(f"Tanggal Lahir: {birth_date}")
    print(f"Masa Jabatan: {start_date} - {end_date}")
    print("-" * 40)
    data = {
        'name' : name,
        'birth' : birth_date,
        'tenure': f'{start_date} - {end_date}',
    }
    president_data.append(data)

    # Copy and save each pres with name, tl, masjab, url pict (if possible) 🐬

for data in president_data:
    fam(data['name'])

keys = president_data[0].keys()
with open("data/wikipedia_data/presidents.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(president_data)

driver.quit()

# Open each detail based on name inside url 🐬