#!/usr/bin/env python3

import os
from configparser import SafeConfigParser
import io
import sys, getopt
from pynput import keyboard

#import all layers
try:
    import layer_1, layer_2, layer_3, layer_4, layer_5
except:
    print('Layer not found in script dir...')

#parse config
configPath = os.path.dirname(os.path.realpath(__file__))+'/config.ini'
config = SafeConfigParser()
config.read(configPath)

stdModKeys = config.get('default', 'stdModKeys').split(',')
keys = config.get('default', 'keys').split(',')
#keys = ["'"+key+"'" for key in keys]
layerKeys = config.get('default', 'layerKeys').split(',')
print(keys)

#generate key combination list and put in list
keyCombs = []
keyComb = []
for key in keys:
    keyComb = stdModKeys + [key]
    keyCombs.append(keyComb)

print(keyCombs)
activeKeys = []

#check if any layer key is active and set layer
def check_if_macro():
    for i, comb in enumerate(keyCombs):
        if set(activeKeys[len(activeKeys)-4:len(activeKeys)]) == set(comb):

            if layerKeys[0] in activeKeys:
                getattr(layer_1, 'macro' + str(i+1))()
                j = '1' 

            elif layerKeys[1] in activeKeys:
                getattr(layer_2, 'macro' + str(i+1))()
                j = '2'
            
            elif layerKeys[2] in activeKeys:
                getattr(layer_3, 'macro' + str(i+1))()
                j = '3'

            elif layerKeys[3] in activeKeys:
                getattr(layer_4, 'macro' + str(i+1))()
                j = '4'

            else:
                getattr(layer_5, 'macro' + str(i+1))()
                j = '0 (Default)'

            print('macro ', i+1, 'from layer ', j)
            break

def on_press(key):
    if str(key) not in activeKeys:
        activeKeys.append(str(key))
        #print(activeKeys)
    #print(key)
    check_if_macro()
    #print('Key {} pressed.'.format(key))

def on_release(key):
    if str(key) in activeKeys:
        activeKeys.remove(str(key))
        #print(activeKeys)
    #print('Key {} released'. format(key))
    
    '''if str(key) == 'Key.esc':
        print('Exiting...')
        return False
    '''
with keyboard.Listener(
    on_press = on_press, on_release = on_release) as listener:
    listener.join()


