import pyscreenshot as ImageGrab
import numpy as np
import cv2
import time

def take_screenshot():
    print("taking screenshot")
    time.sleep(2)

    # only looking at a small portion of the screen to reduce processing time
    screenshot = np.array(ImageGrab.grab(backend="mss", childprocess=False, bbox=(628, 225, 1529, 845)))
    print("screenshot taken")

    return screenshot

def gamma_correction(screenshot):
    gamma_increased = np.power(screenshot, 3)

    cv2.imshow('input', screenshot)
    cv2.imshow('gamma 2', gamma_increased)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
    
    return gamma_increased

def main():
    screenshot = take_screenshot()
    gamma_screenshot = gamma_correction(screenshot)
    

if __name__ == '__main__':
    main()