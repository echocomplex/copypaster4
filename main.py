import pyautogui
import time
import colorama
from colorama import Fore, init
import eel
init()

eel.init("web")

@eel.expose
def func(messages, time1, firstmessage, secondmessage, thirdmessage, fourthmessage):
    print(Fore.LIGHTGREEN_EX + '          DEBUG CONSOLE')
    print(Fore.GREEN + ' -------------------------------')
    print(Fore.GREEN + ' -------------------------------')
    print(Fore.GREEN + ' -------------------------------')
    print(' ')
    try:
        ver = int(messages)
    except:
        print(Fore.LIGHTRED_EX + 'ERROR: You did not enter a number in the message parameter. Error code: 1')
        time.sleep(5)
        quit()
    try:
        tver = float(time1)
    except:
        print(Fore.LIGHTRED_EX + 'ERROR: You did not enter a number in the time parameter. Error code: 2')
        time.sleep(5)
        quit()
    print(Fore.LIGHTYELLOW_EX + 'To end spam just close the program.')
    print(' ')
    if ver == 0:
        a = 0
        while True:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('Enter')
            time.sleep(tver)
            a = a + 1
            print(Fore.CYAN + str(a), 'cycle is completed.')
    if ver == 1:
        a = 0
        while True:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('Enter')
            time.sleep(tver)
            pyautogui.typewrite(firstmessage)
            pyautogui.press('Enter')
            time.sleep(tver)
            a = a + 1
            print(Fore.CYAN + ' ' + str(a), 'cycle is completed.')
    if ver == 2:
        a = 0
        while True:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('Enter')
            time.sleep(tver)
            pyautogui.typewrite(firstmessage)
            pyautogui.press('Enter')
            time.sleep(tver)
            pyautogui.typewrite(secondmessage)
            pyautogui.press('Enter')
            time.sleep(tver)
            a = a + 1
            print(Fore.CYAN + ' ' + str(a), 'cycle is completed.')
    if ver == 3:
        a = 0
        while True:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('Enter')
            time.sleep(tver)
            pyautogui.typewrite(firstmessage)
            pyautogui.press('Enter')
            time.sleep(tver)
            pyautogui.typewrite(secondmessage)
            pyautogui.press('Enter')
            time.sleep(tver)
            pyautogui.typewrite(thirdmessage)
            pyautogui.press('Enter')
            time.sleep(tver)
            a = a + 1
            print(Fore.CYAN + ' ' +  str(a), 'cycle is completed.')
    if ver == 4:
        a = 0
        while True:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('Enter')
            time.sleep(tver)
            pyautogui.typewrite(firstmessage)
            pyautogui.press('Enter')
            time.sleep(tver)
            pyautogui.typewrite(secondmessage)
            pyautogui.press('Enter')
            time.sleep(tver)
            pyautogui.typewrite(thirdmessage)
            pyautogui.press('Enter')
            time.sleep(tver)
            pyautogui.typewrite(fourthmessage)
            pyautogui.press('Enter')
            time.sleep(tver)
            a = a + 1
            print(Fore.CYAN + ' ' +  str(a), 'cycle is completed.')
    else:
        print(Fore.RED + ' ' +  "!!! Critical error! An incorrect value was entered. The program will restart in 5 seconds !!! Error code: 3")
        time.sleep(5)
        quit()

eel.start("main.html", size=(400, 670))