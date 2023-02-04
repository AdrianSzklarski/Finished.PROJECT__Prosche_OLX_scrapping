import pyautogui as py #Import pyautogui
import time


print('Press Ctrl-C to quit.')
try:
    while True:
        print (py.position())
        time.sleep(5)
except KeyboardInterrupt:
    print('\n')