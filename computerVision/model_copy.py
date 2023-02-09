import time
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction():
    start_time = time.time()  # Time at beginning of program - Used for the countdown within get_prediction function
    
    while True: # While loop containing bulk of program
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data, verbose=0)
        # Point between start of program and start of image capture
        cv2.imshow('frame', frame)

        # Find the result using numpy
        result = np.argmax(prediction)
                
        # Assign the result
        if result == 0:
            print("Rock")
            # break
        elif result == 1:
            print("Paper")
            # break
        elif result == 2:
            print("Scissors")
            # break
        elif result == 3:
            print("Nothing")
            # break
        else:
            pass

        # Countdown
        if (time.time() - start_time) < 10:
            print(round((start_time - time.time())*(-1)))
        elif (time.time() - start_time) > 10:
            print("Go!")
            pass
        else:
            pass

        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        
    # After the loop release the cap object
    cap.release()

    # Destroy all the windows
    cv2.destroyAllWindows()

    # Reprint the final result
    print("Final result: ", result)

    # Return the result 
    return result


get_prediction()