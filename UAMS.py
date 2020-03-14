from imutils.video import FileVideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import CNNOperation as cnn
import MathematicalCalculationDLIB as mcd


class UAMS(object):
    """
        Taking a arguments to pass into UAMS
    """
    def argument_init(self):
        ap = argparse.ArgumentParser()
        # Video Input
        # ap.add_argument("-v", "--video", required=True, help="path to video file")
        # prototxt file contains resnet model strucure
        ap.add_argument("-p", "--prototxt", required=True, help="path to model")
        # weights for resnet
        ap.add_argument("-w", "--weights", required=True, help="path to pre-trained weights")
        # can set manually default is 50%
        ap.add_argument("-t", "--threshold", type=float, default=0.5, help="max threshold value for detection")
        self.args = vars(ap.parse_args())


    def UAMS(self):
        # video_file = FileVideoStream(self.args["video"]).start()
        # time.sleep(2.0)
        # fps = FPS().start()
        cap = cv2.VideoCapture(0)
        # while video_file.more():
        while True:
            # Converting each frame to matrix of numbers
            ret, self.frame = cap.read()

            try:
                # self.frame = video_file.read()
                gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
                gray = np.dstack([gray, gray, gray])

            except Exception as e:
                print(e)


            self.frame, self.faces, conf, detection, startX, y = self.cnn_op.CNNOperation(self.frame, self.net, self.args)
            try:
                msg = self.calculation(startX, y)
            except Exception as e:
                print(e)
            try:
                cv2.imshow("frame-this is main frame", self.frame)
            except Exception as e:
                print(e)
            # fps.update()
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

        # print("elapsed time : {:.2f}".format(fps.elapsed()))
        # print("FPS  : {:.2f}".format(fps.fps()))


    def calculation(self, startX, y):
        arrayOfStrings = []
        for i in range(len(self.faces)):
            face, val = self.mcdObj.loopOperation(self.faces[i])
            cv2.imshow("face-array" + str(i), face)
            var = self.conditions(val)
            arrayOfStrings.append(var)
        print(arrayOfStrings)
        return arrayOfStrings

    def conditions(self, val):
        if val == 2:
            return "UN-ATTENTIVE WITH YAWNING"
        elif val == 1:
            return "UN-ATTENTIVE WITH EYES CLOSED"
        else:
            return "ATTENTIVE"

    def __init__(self):
        super(UAMS, self).__init__()
        self.argument_init()
        # self.arrayOfStrings = []
        self.CTR = 5
        self.net = cv2.dnn.readNetFromCaffe(self.args["prototxt"], self.args["weights"])
        self.mcdObj = mcd.MathematicalCalculationDLIB()
        self.cnn_op = cnn.CNNOperation()

        self.UAMS()

        # print("\nJello")
UAMS()
