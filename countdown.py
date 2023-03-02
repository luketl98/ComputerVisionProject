import time
start_time = time.time()
while (time.time() - start_time) < 3:
    print(round(3 - (time.time() - start_time)))