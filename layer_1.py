#!/usr/bin/env python3

import os
import io
from pynput.keyboard import Key, Controller
import pyperclip
import pyautogui

def copyTofile(filename):
    #Read current clipboard to restore later
    oldCb = pyperclip.paste()
    keyboard = Controller()
    #Emulate Ctrl+C
    pyautogui.hotkey('ctrl', 'c')
    newCb = str(pyperclip.paste())
    #Save new clipboard to file '0_1_clp.txt'
    file = open(os.path.dirname(os.path.realpath(__file__))+'/'+filename, 'w')
    file.write(newCb)
    file.close()
    print("Copied:\n'", newCb, "'")
    #Restore old clipboard
    pyperclip.copy(oldCb)

#This is where you define your macros
def macro1():
    copyTofile('0_1_clp.txt')
    
def macro2():
    copyTofile('0_2_clp.txt')

def macro3():
    copyTofile('0_3_clp.txt')

def macro4():
    copyTofile('0_4_clp.txt')

def macro5():
    copyTofile('0_5_clp.txt')

def macro6():
    copyTofile('0_6_clp.txt')

def macro7():
    copyTofile('0_7_clp.txt')

def macro8():
    copyTofile('0_8_clp.txt')

def macro9():
    copyTofile('0_9_clp.txt')

def macro10():
    copyTofile('0_10_clp.txt')

def macro11():
    copyTofile('0_11_clp.txt')

def macro12():
    copyTofile('0_12_clp.txt')

