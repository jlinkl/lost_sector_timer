import pyscreenshot as ImageGrab
import numpy as np
import cv2
import time
# import timer

def take_screenshot():
    print("taking screenshot")
    time.sleep(2)
    # only looking at a small portion of the screen to reduce processing time
    screenshot = np.array(ImageGrab.grab(backend="mss", childprocess=False, bbox=(628, 225, 1529, 845)))
    print("screenshot taken")

    return screenshot

def gamma_correction(screenshot):
    gamma_increased = np.power(screenshot, 10)
    # trying to find if there are non black pixels in the gamma boosted image
    if np.sum(gamma_increased >= 100) != 0:
        # print(f"found {np.sum(gamma_increased > 0)}")
        # by taking note of the time when the starting frame is found, it can be used to find the total time when subtracted from the time of the last frame
        return time.time()
    else:
        # print("not found")
        return -1
    # cv2.imshow('input', screenshot)
    # cv2.imshow('gamma 2', gamma_increased)
    # cv2.waitKey(10000)
    # cv2.destroyAllWindows()

def main():
    screenshot = take_screenshot()
    start_time = gamma_correction(screenshot)
    while start_time > 0:
        pass

if __name__ == '__main__':
    main()