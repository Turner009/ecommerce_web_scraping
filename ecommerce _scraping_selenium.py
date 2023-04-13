from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import csv, operator

file = open('computers_and_laptops.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(["id", "name", "price", "specifications", "number of reviews"])

browser_driver = Service('/Users/mptur/Downloads/chromedriver.exe')
scraper = webdriver.Chrome(service=browser_driver)

scraper.get('https://webscraper.io/test-sites/e-commerce/static/computers/laptops')

element = scraper.find_element(By.CLASS_NAME, 'acceptCookies').click()

id = 1
while True:
    devices = scraper.find_elements(By.CLASS_NAME, 'thumbnail')

    for items in devices:
        name = items.find_element(By.CLASS_NAME, 'title').text
        price = items.find_element(By.CLASS_NAME, 'pull-right.price').text
        price = float(price[1:])
        specs = items.find_element(By.CLASS_NAME, 'description').text
        reviews = items.find_element(By.CLASS_NAME, 'ratings').text
        reviews = int(reviews[:-7])
        writer.writerow([id, name, price, specs, reviews])
        id +=1
        
        

    try:
        element = scraper.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/nav/ul/li[15]/a')
        element.click()
    except NoSuchElementException:
        break

file = sorted(file, key=lambda row:row[2])
file.close()
scraper.quit