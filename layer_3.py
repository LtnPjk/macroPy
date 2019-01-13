#!/usr/bin/env python3

from time import sleep
import os
import io
import pyautogui as pyg

#This is where you define your layers

def macro1():
    pyg.hotkey('ctrl', 'alt', 't')
    sleep(1)
    pyg.typewrite('vi test.txt')
    pyg.hotkey('enter')
    sleep(1)
    pyg.typewrite('i')
    pyg.typewrite('Det här är ett test')
    pyg.hotkey('esc')
    pyg.typewrite(':x')
    pyg.hotkey('enter')
    print('macro1')

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
