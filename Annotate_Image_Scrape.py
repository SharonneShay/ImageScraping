import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os

driver = webdriver.Chrome(executable_path='C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://www.pexels.com/collections/vintage-peu3dul/')
results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
driver.quit()

images = soup.find_all('img')
for image in images:
    link = image['src']
    name = image.find('img')
    print(link, name)
