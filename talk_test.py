import pyautogui
from pywinauto import Application
import time
# print(pyautogui.position())

kakao = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/kakao.png', confidence=0.5)
center_kko = pyautogui.center(kakao)
pyautogui.moveTo(center_kko[0],center_kko[1])
pyautogui.doubleClick()
time.sleep(1.5)

finder = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/finder.png', confidence=0.6)
profile = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/profile.png', confidence=0.6)

center_find = pyautogui.center(finder)
center_pro = pyautogui.center(profile)

partner = pyautogui.prompt("choose your partner")

app = Application().start("C:/Windows/system32/notepad.exe")
app.UntitledNotepad.Edit.type_keys(partner, with_spaces=True)
file = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/file.png', confidence=0.6)
center_file = pyautogui.center(file)
pyautogui.moveTo(center_file[0],center_file[1])
pyautogui.moveRel(None, 20)
pyautogui.doubleClick()
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

pyautogui.moveTo(center_find[0], center_find[1])
pyautogui.moveRel(40, None)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

pyautogui.moveRel(None, 70)
pyautogui.doubleClick()
time.sleep(0.5)

pyautogui.moveTo(center_file[0],center_file[1])
pyautogui.moveRel(None, 20)
pyautogui.doubleClick()
while 1:
    exam1 = "점심 챙겨먹어야대!! 나도 이제 밥먹으러가! 사랑해!!"
    exam2 = "오후도 힘내야대!! 시간나면 연락해!!"
    text = pyautogui.prompt("send your message")
    if text == "e":
        break
    if text == "1":
        app.UntitledNotepad.Edit.type_keys(exam1, with_spaces=True)
    elif text == "2":
        app.UntitledNotepad.Edit.type_keys(exam2, with_spaces=True)
    else:
        app.UntitledNotepad.Edit.type_keys(text, with_spaces=True)
    pyautogui.press('enter')


pyautogui.moveTo(center_file[0],center_file[1])
pyautogui.moveRel(None, 20)
pyautogui.moveRel(-20, None)
pyautogui.dragTo(pyautogui.position()[0]+300, pyautogui.position()[1]+60, duration=0.5)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

give = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/give.png', confidence=0.6)
center_give = pyautogui.center(give)
pyautogui.moveTo(center_give[0], center_give[1])
pyautogui.moveRel(-200, None)
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
time.sleep(0.5)

pyautogui.moveTo(center_find[0], center_find[1])
pyautogui.moveRel(40, None)
pyautogui.doubleClick()
pyautogui.hotkey('delete')
time.sleep(1)

close = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/close.png', confidence=0.9)
center_close = pyautogui.center(close)
pyautogui.moveTo(center_close[0], center_close[1])
pyautogui.moveRel(None, -35)
pyautogui.click()
time.sleep(0.5)

kko_close = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/kko_close.png', confidence=0.8)
center_kko_close = pyautogui.center(kko_close)
pyautogui.moveTo(center_kko_close[0], center_kko_close[1])
pyautogui.moveRel(None, -35)
pyautogui.moveRel(20,None)
pyautogui.click()







