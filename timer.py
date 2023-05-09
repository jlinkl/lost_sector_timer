import time

def main():

    frame = (1.0/60.0)
    # frame = 0.016

    y = 0   
    stop = False

    # while the condition for stopping the timer is false, increment the timer, and then check to see if the condition for stopping the timer is met
    while y <= 3.0:
        y += frame
        seconds = int(y % 60)
        minutes = int(y / 60) % 60
        milliseconds = int((y % 1) * 1000)
        print(f"{minutes:02}:{seconds:02}:{milliseconds:03}")

        # time.sleep(frame)

    print("stopped")

if __name__ == '__main__':
    main()

