import cv2
import numpy as np
import os
import threading
import subprocess
import sys


def scanner():
    oldData = ''
    img = cv2.VideoCapture(0)
    
    os.system('cls')
    while True:
        detector = cv2.QRCodeDetector()
        s, imgOG = img.read()
        H_len = np.shape(imgOG)[1]

        data, points, straight_qrcode = detector.detectAndDecode(imgOG)
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
                print(point1)
                print(point2)
                cv2.line(imgOG, point1, point2, color=(255, 0, 0),
                         thickness=3)  # makes box around qr

                if i == 0:  # prints text on box
                    x, y = ((point1[0]//2 + point2[0]//2) - len(data) //
                            2*13, (point1[1]//2 + point2[1]//2) - 10)
                    cv2.putText(imgOG, data, (x, y),
                                cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 0), 2)
                if len(data) >= 1 and data!= oldData:
                    p = subprocess.Popen([sys.executable, 'playCurrentAudio.py', data], 
                                         stdout=subprocess.PIPE, 
                                         stderr=subprocess.STDOUT)
                    oldData = data = ''
                    # cv2.destroyAllWindows()

        else:
            imgOG = cv2.flip(imgOG, 1)

        cv2.imshow("Video", imgOG)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # exits code when 'q' is pressed
            cv2.destroyAllWindows()
            break

def f3(frame1, frame3):
    th1 = threading.Thread(target=scanner).start()
