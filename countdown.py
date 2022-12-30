import time
#import model_checking_file as mcf
#import camera_rps as cam_rps

def countdown():
    max_time = 3
    start_time = time.time()
    while (time.time() - start_time) < max_time:
        #cam_rps
        print(time.time())
    pass

countdown()

