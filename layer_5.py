#!/usr/bin/env python3

import os
import io
import pyautogui
import pyperclip

def pasteFromFile(filename):
    try:
        #Read content of '0_1_clp.txt' and paste
        oldCb = pyperclip.paste()
        file = open(os.path.dirname(os.path.realpath(__file__))+'/'+filename, 'r')
        newCb = file.read()
        file.close()
        pyperclip.copy(newCb)
        pyautogui.hotkey('ctrl', 'v')
        print('Pasted: ', newCb)
        pyperclip.copy(oldCb)
    except:
        print('FILE NOT FOUND!')

#This is where you define your layers
def macro1():
    pasteFromFile('0_1_clp.txt')

def macro2():
    pasteFromFile('0_2_clp.txt')

def macro3():
    pasteFromFile('0_3_clp.txt')

def macro4():
    pasteFromFile('0_4_clp.txt')

def macro5():
    pasteFromFile('0_5_clp.txt')

def macro6():
    pasteFromFile('0_6_clp.txt')

def macro7():
    pasteFromFile('0_7_clp.txt')

def macro8():
    pasteFromFile('0_8_clp.txt')

def macro9():
    pasteFromFile('0_9_clp.txt')

def macro10():
    pasteFromFile('0_10_clp.txt')

def macro11():
    pasteFromFile('0_11_clp.txt')

def macro12():
    pasteFromFile('0_12_clp.txt')
