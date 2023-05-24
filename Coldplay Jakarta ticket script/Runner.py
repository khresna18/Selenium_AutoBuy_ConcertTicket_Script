import os
import datetime
import pytz
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Coldplaywinner(url, button_xpath):
    driver = webdriver.Chrome()
    driver.get(url)
    button = driver.find_element(By.XPATH, button_xpath)
    button.click()
    time.sleep(9999999999999999999999999999999999999999999999999999)

    

# Example usage
url = "https://www.youtube.com/"
button = "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]"

Coldplaywinner(url, button)
