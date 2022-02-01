from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")


## Set path to chromedirver as per your configuration
webdriver_service = Service('/home/fihyer//chromedriver/stable/chromedriver')

## Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

## Get page
browser.get('http://localhost:8000')

assert "Congratulations" in browser.title