import time
"""
def countdown():

    while countdown > 0:
        print ('CountDown = ', countdown)
        if countdown == 3:
            break
"""

def timer():
    
    max_time = 4
    start_time = time.time()
    while (time.time() - start_time) < max_time:
        # print(round(start_time - time.time())*(-1))
        if (round(time.time() - start_time)) == 0:
            print("3")
        elif (round(time.time() - start_time)) == 1:
            print("2")
        elif (round(time.time() - start_time)) == 2:
            print("1")
        elif (round(time.time() - start_time)) == 3:
            print("Go")
        else:
            break





timer()