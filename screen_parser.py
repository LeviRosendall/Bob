import cv2
import pytesseract
import mss
import numpy as np
from time import sleep

class ScreenParser():
    def __init__(self) -> None:
        # Part of the screen to capture
        self.monitor = {"top": 832, "left": 40, "width": 120, "height": 10}
        #3024 × 1964
        self.heading = []
        self.x_coord = []
        self.y_coord = []

        self.heading_patience = 0
        self.x_patience = 0
        self.y_patience = 0

    def parse(self, sct):
      
        img = np.array(sct.grab(self.monitor))
        # img = cv2.resize(img, dsize=(150, 50))
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.bitwise_not(img)

        h,w,hbb = np.shape(img)

        for py in range(0,h):
            for px in range(0,w):
                if (img[py][px][0] < 50) & (img[py][px][1] < 50) & (img[py][px][2] < 50):
                    img[py][px][0] = 0
                    img[py][px][1] = 0
                    img[py][px][2] = 0
                else:
                    img[py][px][0] = 255
                    img[py][px][1] = 255
                    img[py][px][2] = 255

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Display the picture
        # cv2.imshow("OpenCV/Numpy normal", img)
        coord_string = pytesseract.image_to_string(img)
        alnum_str = ''.join(letter for letter in coord_string if letter.isdigit() | (letter == ',') | (letter == '.'))
        
        number_list = alnum_str.split(',') 
        # further refinement of values
        if len(number_list) == 3:
            try: 
                if len(self.heading) > 10:
                    if (float(number_list[0]) >= 0) & (float(number_list[0]) <= 360):
                        if abs(float(number_list[0]) - self.heading[0]) < 50:
                            self.heading.insert(0, float(number_list[0]))
                        else:
                            self.heading_patience += 1
                            if self.heading_patience > 10:
                                self.heading.insert(0, float(number_list[0]))
                                self.heading_patience = 0
                else:
                    self.heading.insert(0, float(number_list[0]))
            except:
                pass
            
            try: 
                if len(self.x_coord) > 10:
                    if (int(number_list[1]) >= 0) & (int(number_list[1]) <= 2000):
                        if abs(int(number_list[1]) - self.x_coord[0]) < 500:
                            self.x_coord.insert(0, int(number_list[1]))
                        else:
                            self.x_patience += 1
                            if self.x_patience > 3:
                                self.x_coord.insert(0, int(number_list[1]))
                                self.x_patience = 0
                else:
                    self.x_coord.insert(0, int(number_list[1]))
            except:
                pass

            try: 
                if len(self.y_coord) > 10:
                    if (int(number_list[2]) >= 0) & (int(number_list[2]) <= 2000):
                        if abs(int(number_list[2]) - self.y_coord[0]) < 500:
                            self.y_coord.insert(0, int(number_list[2]))
                        else:
                            self.y_patience += 1
                            if self.y_patience > 3:
                                self.y_coord.insert(0, int(number_list[2]))
                                self.y_patience = 0
                else:
                    self.y_coord.insert(0, int(number_list[2]))
            except:
                pass
        try:
            print(f"heading: {self.heading[0]}")
            print(f"x_coord: {self.x_coord[0]}")
            print(f"y_coord: {self.y_coord[0]}")
        except:
            pass


        # # Press "q" to quit
        # if cv2.waitKey(25) & 0xFF == ord("q"):
        #     cv2.destroyAllWindows()
        #     break
        