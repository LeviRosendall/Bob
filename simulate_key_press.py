from pynput.keyboard import Controller
import time
import random

keyboard = Controller()

def hold_key(key, hold_duration):
    keyboard.press(key)
    time.sleep(hold_duration)
    keyboard.release(key)

print('5')
time.sleep(1)   
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
for i in range(1, 100):
    hold_key('w', 0.05)