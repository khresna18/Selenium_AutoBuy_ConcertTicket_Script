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
    current_url = driver.current_url
    button.click()
    new_url = driver.current_url
    if current_url == new_url:
        driver.close()
    else:
        while True:
            time.sleep(1)

    

# Example usage
url = "https://coldplayinjakarta.com/"
button = "/html/body/div/div/div[1]/div/div/div[5]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div"



#youtube cobtoh
#url = "https://youtube.com/"
#button = "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]"

Coldplaywinner(url, button)
