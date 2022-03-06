import numpy as np
import cv2
import time
import os

# the index depends on your camera setup and which one is your USB camera.
cap = cv2.VideoCapture(0)

while(True):
    time.sleep(2)

    filename = datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".png"

    # Capture frame-by-frame
    ret, frame = cap.read()
    frame.imwrite(filename)

    # rc,png = cv2.imencode('.png', face)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
