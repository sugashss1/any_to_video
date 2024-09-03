import cv2
import numpy as np
def video_to_binary(video_path,file_path):
    cap = cv2.VideoCapture(video_path)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    array_of_image = np.empty((frameWidth,frameHeight, 3), np.dtype('uint8'))

    fc = 0
    ret = True
    f = open(file_path, "wb")
    f.write(array_of_image.tobytes())
    while (fc < frameCount  and ret):
        ret, array_of_image = cap.read()
        fc += 1
        f.write(array_of_image.tobytes())
    cap.release()
    cv2.waitKey(0)
    f.close()
binary_video_path = input("enter path to bin video:")
file_path = input("give path of file:")
video_to_binary(binary_video_path,file_path)