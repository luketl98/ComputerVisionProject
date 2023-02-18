# 3 second Countdown     --------      # print(round((start_time - time.time())*(-1)))
import time

start_time = time.time()
one = 0
two = 0
three = 0
while (time.time() - start_time) < 3:
    if one == 1:
        pass
    elif round(time.time() - start_time) == 1:
        print(1)
        one = 1
    # ----------------
    if two == 2:
        pass
    elif round(time.time() - start_time) == 2:
        print(2)
        two = 2
    # ----------------
    if three == 3:
        pass
    elif round(time.time() - start_time) == 3:
        print(3)
        three = 3
else:
    pass
