import pyautogui
import time
from pywinauto.application import Application
import pyperclip

# print(pyautogui.position())
input_text=pyautogui.prompt("write text")
input_site_name = pyautogui.prompt("choice site(n = naver, g = google)")
if input_site_name == "n":
    input_site_name = "naver.com"
elif input_site_name == "g":
    input_site_name = "google.co.kr"
time.sleep(0.5)

app = Application().start("C:/Windows/system32/notepad.exe")
app.UntitledNotepad.Edit.type_keys(input_site_name, with_spaces=True)
file = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/file.png', confidence=0.6)
center_file = pyautogui.center(file)
pyautogui.moveTo(center_file[0],center_file[1])
pyautogui.moveRel(None, 20)
pyautogui.doubleClick()
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

google = pyautogui.locateOnScreen("C:/Users/qodls/PycharmProjects/auto/data/google.png", confidence=0.5)
center_gg = pyautogui.center(google)
pyautogui.moveTo(center_gg[0],center_gg[1])
pyautogui.doubleClick()
time.sleep(0.5)

finder = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/naver.png', confidence=0.8)
center_find = pyautogui.center(finder)
pyautogui.moveTo(center_find[0], center_find[1])
pyautogui.moveRel(80, None)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(1)

pyperclip.copy(input_text)
search = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/search.png', confidence=0.6)
center_search = pyautogui.center(search)
pyautogui.moveTo(center_search[0],center_search[1])
pyautogui.moveRel(-300,None)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(0.5)

app.UntitledNotepad.menu_select("파일(&F)->끝내기(&X)")
time.sleep(0.1)
no_save = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/no_save.png', confidence=0.5)
center_no_save = pyautogui.center(no_save)
pyautogui.moveTo(center_no_save[0], center_no_save[1])
pyautogui.click()




