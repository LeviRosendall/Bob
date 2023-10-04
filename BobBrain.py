from screen_parser import ScreenParser
from pynput.keyboard import Controller
import time
import mss
import threading

def hold_key(keys, hold_duration):
    if len(keys) < 2:
        keys = ['w', 'l']
    with keyboard.pressed(keys[0]):
        keyboard.press(keys[1])
        time.sleep(hold_duration)
        keyboard.release(keys[1])


screen_parser = ScreenParser()

keyboard = Controller()

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


with mss.mss() as sct:
    for i in range(2000):
        try:
            try:
                t1.join()
            except:
                pass
            screen_parser.parse(sct)
            heading = screen_parser.heading[0]
            x_coord = screen_parser.x_coord[0]
            y_coord = screen_parser.y_coord[0]

            keys_to_press = ['w']

            if y_coord < 1111:
                if heading < 92:
                    keys_to_press.append('d')
            elif y_coord > 1111:
                if heading > 88:
                    keys_to_press.append('a')
            else:
                keys_to_press.append('l')
            
            print(keys_to_press)
            t1 = threading.Thread(target=hold_key, args=(keys_to_press, 0.2,))
            t1.start()
        except:
            pass#print(i)
    

