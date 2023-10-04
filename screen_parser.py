import cv2
import pytesseract
import mss
import numpy as np

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 832, "left": 50, "width": 100, "height": 10}
    #3024 × 1964
    while True:
    
        img = np.array(sct.grab(monitor))
        # img = cv2.resize(img, dsize=(150, 50))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.bitwise_not(img)

        h,w = np.shape(img)

        for py in range(0,h):
            for px in range(0,w):
                if img[py][px] < 50:
                    img[py][px] = 0
                else:
                    img[py][px] = 255

        
        # Display the picture
        cv2.imshow("OpenCV/Numpy normal", img)
        coord_string = pytesseract.image_to_string(img)
        test_str = ''.join(letter for letter in coord_string if letter.isalnum() | (letter == ',') | (letter == '.'))
        
        
        print(test_str)
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break