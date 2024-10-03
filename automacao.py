import pyautogui
import subprocess
import time

url_formulario = "https://forms.office.com/r/PwS0k9yyqs?origin=lprLink"

subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

time.sleep(1)
pyautogui.write(url_formulario)

time.sleep(1)
pyautogui.press('enter')

time.sleep(1)
#pyautogui.press('tab')
#pyautogui.press('tab')

time.sleep(0.5)
pyautogui.write("Carlos")
pyautogui.press('tab')

time.sleep(0.5)
pyautogui.write("Mozlista")
pyautogui.press('tab')

time.sleep(0.5)
pyautogui.write("Programador")
pyautogui.press('tab')

pyautogui.press('enter')