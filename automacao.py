import pyautogui
import subprocess
import time

url_formulario = "https://forms.office.com/r/PwS0k9yyqs?origin=lprLink"

subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

time.sleep(1)
pyautogui.write(url_formulario)

pyautogui.press('enter')
