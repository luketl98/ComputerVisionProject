import time
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction():
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data, verbose=0)

        # Period of time between start of program and start of image capture

        cv2.imshow('frame', frame)

        # Find the result using numpy
        result = np.argmax(prediction)

        # Countdown
        start_time = time.time()
        while (time.time() - start_time) < 3:
            print(round((start_time - time.time())*(-1)))
        
                
        # Assign the result
        if result == 0:
            result = 'Rock'
            # break
        elif result == 1:
            result = "Paper"
            # break
        elif result == 2:
            result = "Scissors"
            # break
        elif result == 3:
            result = "Nothing"
            # break

        # print result
        # print(result)

        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # Breaks program once 3 second countdown is up
        elif (time.time() - start_time) > 3:
            break
        
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    # Reprint the result
    print("Final result: ", result)

    # Return the result 
    return result
    



def countdown():
    max_time = 3
    start_time = time.time()
    while (time.time() - start_time) < max_time:
        # print(round((start_time - time.time())*(-1)))
        if (time.time() - start_time) >= max_time:
            break



get_prediction()