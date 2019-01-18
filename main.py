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

    def anish(self, frame, net, args):
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


class UAMS(object):
    """docstring for UAMS"""

    def argument_init(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-v", "--video", required=True, help="path to video file")
        ap.add_argument("-p", "--prototxt", required=True, help="path to model")
        ap.add_argument("-w", "--weights", required=True, help="path to pre-trained weights")
        ap.add_argument("-t", "--threshold", type=float, default=0.5, help="max threshold value for detection")
        self.args = vars(ap.parse_args())

    def UAMS(self):
        video_file = FileVideoStream(self.args["video"]).start()
        time.sleep(2.0)

        fps = FPS().start()

        while video_file.more():

            frame = video_file.read()
            self.frame = imutils.resize(frame, width=500)
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            gray = np.dstack([gray, gray, gray])
            frame = self.cnn_op.anish(self.frame, self.net, self.args)
            cv2.imshow("frame", frame)
            fps.update()
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        fps.stop()
        print("elapsed time : {:.2f}".format(fps.elapsed()))
        print("FPS  : {:.2f}".format(fps.fps()))

    def __init__(self):
        super(UAMS, self).__init__()
        self.argument_init()
        self.net = cv2.dnn.readNetFromCaffe(self.args["prototxt"], self.args["weights"])
        self.cnn_op = CNNOperation()

        self.UAMS()

        # print("\nJello")
UAMS()
