import numpy as np
import cv2
import pyautogui
import time

index = 0
threshold = 0.8

#put images names in the correct order in the images array, include file extensions
images = ["put", "images", "here"]
while True:
    if index > len(images) - 1:
        index = 0
    print(images[index] + "\n")
    symbol_image = cv2.imread(images[index])
    
    # Capture the screen using pyautogui
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform symbol detection (template matching)
    result = cv2.matchTemplate(frame, symbol_image, cv2.TM_CCOEFF_NORMED)

    loc = np.where(result >= threshold)

    if len(loc[0]) > 0:
        # Symbol detected, click the mouse at the first location
        x, y = loc[1][0], loc[0][0]
        symbol_height, symbol_width, _ = symbol_image.shape

        # Adjusted x and y coordinate to center
        x_center = x + symbol_width // 2  
        y_center = y + symbol_height // 2  
        pyautogui.click(x_center, y_center)
        index += 1
        #may want to add a delay here with time.sleep


    # Exit if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

