import cv2
import numpy as np
import subprocess, sys
from assets.src import config

def scan(imgOG):
    detector = cv2.QRCodeDetector()
    H_len = np.shape(imgOG)[1]

    config.Data, points, straight_qrcode = detector.detectAndDecode(imgOG)
    if points is not None:
        imgOG = cv2.flip(imgOG, 1)

        points = np.ndarray.tolist(points)
        points = points[0]
        n_lines = len(points)  # simpifies points array/list

        for i in range(n_lines):  # converts floats into ints
            points[i] = [round(a) for a in points[i]]

        for i in points:  # flips lines horizontally
            i[0] = H_len - i[0]

        for i in range(n_lines):
            point1 = tuple(points[i])
            point2 = tuple(points[(i+1) % n_lines])
            cv2.line(imgOG, point1, point2, color=(255, 0, 0),
                        thickness=3)  # makes box around qr

            if i == 0:  # prints text on box
                x, y = ((point1[0]//2 + point2[0]//2) - len(config.Data) //
                        2*13, (point1[1]//2 + point2[1]//2) - 10)
                cv2.putText(imgOG, config.Data, (x, y),
                            cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 0), 2)
            if len(config.Data) >= 1 and config.Data!= config.oldData:
                print("playing audio")
                subprocess.Popen([sys.executable, 'src/playCurrentAudio.py', config.Data],)
                config.oldData = config.Data = ''

    else:
        imgOG = cv2.flip(imgOG, 1)
    return imgOG