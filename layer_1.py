#!/usr/bin/env python3

import os
import io
from pynput.keyboard import Key, Controller
import pyperclip
import pyautogui

#This is where you define your macros
def macro1():
    #Read current clipboard to restore later
    oldCb = pyperclip.paste()
    keyboard = Controller()
    #Emulate Ctrl+C
    pyautogui.hotkey('ctrl', 'c')
    newCb = str(pyperclip.paste())
    #Save new clipboard to file '0_1_clp.txt'
    file = open(os.path.dirname(os.path.realpath(__file__))+'/0_1_clp.txt', 'w')
    file.write(newCb)
    file.close()
    print("Copied:\n'", newCb, "'")
    #Restore old clipboard
    pyperclip.copy(oldCb)

def macro2():
    print('macro2')

def macro3():
    print('macro3')

def macro4():
    print('macro4')

def macro5():
    print('macro5')

def macro6():
    print('macro6')

def macro7():
    print('macro7')

def macro8():
    print('macro8')

def macro9():
    print('macro9')

def macro10():
    print('macro10')

def macro11():
    print('macro11')

def macro12():
    print('macro12')

