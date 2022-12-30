import time
import camera_rps

def countdown():
    max_time = 3
    start_time = time.time()
    while (time.time() - start_time) < max_time:
        get_prediction()
    pass

countdown()

