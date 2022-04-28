import numpy as np
import cv2
import time
import os
from datetime import datetime
from PIL import Image
import subprocess

NUM_OF_IMAGES = 20
SECONDS_BETWEEN_IMAGES = 2

# the index depends on your camera setup and which one is your USB camera.
cap = cv2.VideoCapture(0)
print("Warning up camera...")
i = 0
while(i < 5):
    i += 1
    # Capture frame-by-frame
    ret, frame = cap.read()
    time.sleep(5)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

i = 0
while(i < NUM_OF_IMAGES):
    i += 1
    filename = "img_" + str(datetime.utcnow()) + ".png"

    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("failed capturing image")
    else:
        cv2.imwrite(filename, frame)
        print("Captured image " + filename)

    time.sleep(SECONDS_BETWEEN_IMAGES)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

files = np.array(os.listdir())[["img_" in file for file in os.listdir()]]
files.sort()
images = [Image.open(file) for file in files]

images[0].save(
    "timelapse.gif",
    save_all=True,
    append_images=images[1:],
    optimize=False,
    duration=len(images)*80,
    loop=0)

subprocess.run("git add timelapse.gif".split(), stdout=subprocess.PIPE)
subprocess.run("git commit -m another_upload".split(), stdout=subprocess.PIPE)
subprocess.run("git push".split(), stdout=subprocess.PIPE)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
