import pyautogui
import time

def arahinklik(x, y) :
    pyautogui.moveTo(x, y)
    pyautogui.click()
    

def arahinkliklong(x, y, sleep) :
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    time.sleep(sleep)
    pyautogui.mouseUp()
      

arahinklik(87, 52)
time.sleep(1)
arahinkliklong(1358, 280, 0.5)
arahinklik(812,517)
arahinklik(509, 15)
text = "https://coldplayinjakarta.com/"
pyautogui.typewrite(text)
pyautogui.press('enter')
time.sleep(1)
arahinkliklong(1358, 280, 0.5)
arahinklik(812,517)
arahinklik(747,17)
pyautogui.typewrite(text)
pyautogui.press('enter')
time.sleep(1)
arahinkliklong(1358, 280, 0.5)
arahinklik(812,517)


# Move the cursor to the center of the screen

