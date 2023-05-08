import time

frame = (1.0/60.0)

y = 0
for x in range(60):
    y += frame
    time.sleep(frame)

print(y)

