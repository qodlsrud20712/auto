import pyautogui
import time
from pywinauto.application import Application
#
kakao = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/kakao.png', confidence=0.5)
google = pyautogui.locateOnScreen("C:/Users/qodls/PycharmProjects/auto/data/google.png", confidence=0.5)
pycharm = pyautogui.locateOnScreen("C:/Users/qodls/PycharmProjects/auto/data/pycharm.png", confidence=0.5)


center_kko = pyautogui.center(kakao)
center_gg = pyautogui.center(google)
center_pc = pyautogui.center(pycharm)


pyautogui.moveTo(center_gg[0],center_gg[1])
pyautogui.doubleClick()
time.sleep(0.5)

pyautogui.moveTo(center_pc[0],center_pc[1])
pyautogui.doubleClick()
time.sleep(0.5)

app = Application().start("C:/Windows/system32/notepad.exe")
app.UntitledNotepad.Edit.type_keys("poki159357", with_spaces=True)

file = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/file.png', confidence=0.6)
center_file = pyautogui.center(file)

pyautogui.moveTo(center_file[0],center_file[1])
pyautogui.moveRel(None, 20)
pyautogui.doubleClick()
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

pyautogui.moveTo(center_kko[0],center_kko[1])
pyautogui.doubleClick()
time.sleep(1)

login = pyautogui.locateOnScreen("C:/Users/qodls/PycharmProjects/auto/data/login.png", confidence=0.8)
center_login = pyautogui.center(login)
pyautogui.moveTo(center_login[0],center_login[1])
pyautogui.moveRel(None, -40)
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

