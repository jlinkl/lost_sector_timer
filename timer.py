import time

y = 0
for x in range(20):
    y = y + 0.016
    time.sleep(0.016)
    print(y)
    y += 0.017
    time.sleep(0.017)
    print(y)
    y += 0.017
    time.sleep(0.017)
    print(y)

