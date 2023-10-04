from pynput.keyboard import Controller
import time
import random

keyboard = Controller()

def hold_key(keys, hold_duration):
    with keyboard.pressed(keys[0]):
        keyboard.press(keys[1])
        time.sleep(hold_duration)
        keyboard.release(keys[1])

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
    hold_key(['w', 'a'], 0.25)