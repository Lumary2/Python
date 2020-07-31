import pyautogui, time
from selenium import webdriver

driver= webdriver.Firefox()
driver.get('http://127.0.0.1:5000/')


pyautogui.click(611,344)
pyautogui.typewrite("Hermine" + '\t')
pyautogui.typewrite("Granger" + '\t')
pyautogui.typewrite(['down','tab',' '])

pyautogui.press('tab')
pyautogui.click(654,601)

#close window
#pyautogui.hotkey('ctrl','q')
