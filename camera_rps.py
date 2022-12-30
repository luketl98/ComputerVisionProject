import cv2
from keras.models import load_model
import numpy as np
import time
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
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        print(prediction)

    # Find the result using numpy and print
        result = np.argmax(prediction)
        print(result)

    # Assign the result
        if result == 0:
            result = "Rock"
            print(result)
        elif result == 1:
            result = "Paper"
            print(result)
        elif result == 2:
            result = "Scissors"
            print(result)
        elif result == 3:
            result = "Nothing"
            print(result)
            
        
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    # Reprint the result
    print(result)
    # Return the result 
    return result



def countdown():
    get_prediction
    max_time = 3
    start_time = time.time()
    while (time.time() - start_time) < max_time:
        get_prediction()
    pass

countdown()