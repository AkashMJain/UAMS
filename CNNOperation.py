from imutils.video import FileVideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2


class CNNOperation(object):
    """docstring for CNNOperation"""

    def __init__(self):
        super(CNNOperation, self).__init__()
        # self.arg = arg

    def CNNOperation(self, frame, net, args):
        faces = []
        (h, w) = frame.shape[: 2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detection = net.forward()
        for face in range(0, detection.shape[2]):
            conf = detection[0, 0, face, 2]
            if conf < args["threshold"]:
                continue

            box = detection[0, 0, face, 3: 7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 1)

            # frame = window[sY - 10:eY + 10, sX - 10:eX + 10]

            temp = frame[startY - 10:endY + 10, startX - 10:endX + 10]

            faces.append(temp)

        return frame
