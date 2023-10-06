from screen_parser import ScreenParser
from pynput.keyboard import Controller
import time
import mss
import threading
import math
import numpy as np

def hold_key(keys, hold_duration):
    if len(keys) < 2:
        keys = ['w', 'l']
    with keyboard.pressed(keys[0]):
        keyboard.press(keys[1])
        time.sleep(hold_duration)
        keyboard.release(keys[1])

def get_to_next_point(destination, current_point, heading):
    x_dest, y_dest = destination
    x, y = current_point

    x_diff = x_dest - x
    y_diff = y_dest - y

    angle = np.arctan2([y_diff], [x_diff]) * 180 / np.pi + 90
    angle = angle[0] % 360
    print(f"angle {angle}")
    print(f"heading {heading}")

    # do i turn left or right
    # right if angle is between heading and heading + 180 %360
    # left if angle is between heading + 180 %360 and heading

    # if (angle > heading - 180 % 360) and (angle < heading):
    #     print('turn left')
    #     press_length = abs(angle-heading)/180
    #     if press_length > 0.2:
    #         press_length = 0.2
    #     return ('a', press_length)
    # elif (angle > heading) and (angle < heading + 180 % 360):
    #     print('turn right')
    #     press_length = abs(angle-heading)/180
    #     if press_length > 0.2:
    #         press_length = 0.2
    #     return ('d', press_length)
    # else:
    #     return ('l', 0.1)

    angle_diff = (heading - angle) % 360
    
    press_length = abs(angle-heading)/360
    if press_length > 0.15:
        press_length = 0.15
    elif press_length < 0.05:
        press_length = 0.05
    

    if (angle_diff >= 180) and (angle_diff <= 360):
        print('turn right')
        return ('d', press_length)
    elif (angle_diff >= 0) and (angle_diff <= 180):
        print('turn left')
        return ('a', press_length)
    else:
        return ('l', 0.1)






    

screen_parser = ScreenParser()

keyboard = Controller()

# route = [(1020, 1103), (1020,1116), (1700,1116), (1700,1103)]

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
threads_started = 0

with mss.mss() as sct:
    for i in range(100):
        try:
            
            screen_parser.parse(sct)
            heading = screen_parser.heading[0]
            x_coord = screen_parser.x_coord[0]
            y_coord = screen_parser.y_coord[0]

            keys_to_press = ['w']

            try:
                feedback = get_to_next_point((1800,1110), (x_coord, y_coord), heading)
                print(feedback)
                keys_to_press.append(feedback[0])
            except:
                feedback = ('l', 0.1)
                print('Error Steering')

            if threads_started == 1:
                t1.join()
            hold_key(['k', 'l'], 0.05)
            t1 = threading.Thread(target=hold_key, args=(keys_to_press, feedback[1],))
            t1.start()

            threads_started = 1
        except:
            pass#print(i)
    

