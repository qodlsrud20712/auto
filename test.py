import pyautogui
from pywinauto import Application
import time
import pyperclip


# test=pyautogui.prompt()
# print(test)
# print(type(test))

app = Application().start("C:/Windows/system32/notepad.exe")
# app.UntitledNotepad.Edit.type_keys(test, with_spaces=True)

time.sleep(0.5)

file = pyautogui.locateOnScreen('C:/Users/qodls/PycharmProjects/auto/data/file.png', confidence=0.8)
center_file = pyautogui.center(file)
pyautogui.moveTo(center_file[0],center_file[1])
pyautogui.moveRel(None, 20)
pyautogui.doubleClick()
while 1:
    exam1 = "점심 챙겨먹어야대!! 나도 이제 밥먹으러가! 사랑해!!"
    exam2 = "오후도 힘내야대!! 시간나면 연락해!!"
    test = pyautogui.prompt()
    if test == "1":
        app.UntitledNotepad.Edit.type_keys(exam1, with_spaces=True)
    elif test == "2":
        app.UntitledNotepad.Edit.type_keys(exam2, with_spaces=True)
    else:
        app.UntitledNotepad.Edit.type_keys(test, with_spaces=True)
    pyautogui.press('enter')
    if test == "end":
        break

