#!/usr/bin/env python3

import os
import io
import pyautogui
import pyperclip

#This is where you define your layers

def macro1():
    #Read content of '0_1_clp.txt' and paste
    oldCb = pyperclip.paste()
    file = open(os.path.dirname(os.path.realpath(__file__))+'/0_1_clp.txt', 'r')
    newCb = file.read()
    file.close()
    pyperclip.copy(newCb)
    pyautogui.hotkey('ctrl', 'v')
    print("Pasted:\n'", newCb,"'")
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
