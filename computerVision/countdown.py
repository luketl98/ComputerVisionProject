import time

def timer():
    
    max_time = 4
    start_time = time.time()
    while max_time > 0:
        difference = time.time() - start_time

        if 1 > difference > 0:
            print(max_time)
        
        if 2 > difference > 1:
            max_time = 3
            print(max_time)
        
        elif 3 > difference > 2:
            max_time = 2
            print(max_time)
        
        elif 4 > difference > 3:
            max_time = 1
            print(max_time)
        
        elif 5 > difference > 4:
            print('Go')
            break
            
timer()