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
    """docstring for UAMS"""

    def argument_init(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-v", "--video", required=True, help="path to video file")
        ap.add_argument("-p", "--prototxt", required=True, help="path to model")
        ap.add_argument("-w", "--weights", required=True, help="path to pre-trained weights")
        ap.add_argument("-t", "--threshold", type=float, default=0.5, help="max threshold value for detection")
        self.args = vars(ap.parse_args())
        # return args

    def UAMS(self):
        video_file = FileVideoStream(self.args["video"]).start()
        time.sleep(2.0)

        fps = FPS().start()

        while video_file.more():

            frame = video_file.read()
            self.frame = imutils.resize(frame, width=500)
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            gray = np.dstack([gray, gray, gray])

            if self.CTR == 5:
                self.frame, startX, startY, endX, endY, self.faces, conf = self.cnn_op.CNNOperation(self.frame, self.net, self.args)

                try:
                    msg = self.calculation()

                    # text = "{:.2f}%".format(conf * 100) + self.calculation()
                except Exception as e:
                    print(e)

                # self.calculation()
                self.CTR = 0
            else:
                self.CTR = self.CTR + 1
            text = "hi there"
            # if CTR == 5:
            cv2.putText(self.frame, text, (startX, startY), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
            cv2.imshow("frame", self.frame)
            fps.update()
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        fps.stop()
        print("elapsed time : {:.2f}".format(fps.elapsed()))
        print("FPS  : {:.2f}".format(fps.fps()))

        # For images un comment followings

        # while True:
        #     key = cv2.waitKey(1) & 0xFF
        #     if key == ord("q"):
        #         break
    def calculation(self):
        arrayOfStrings = []
        for i in range(len(self.faces)):
            face, val = self.mcdObj.loopOperation(self.faces[i])
            # print("FACE ID : " + str(i) + " value is : " + str(val))
            # self.face.append(face)
            # for i in range(self.faces):
            cv2.imshow("face-array" + str(i), face)
            # print("Number of faces :- " + str(len(self.faces)))

            var = self.conditions(val)
            arrayOfStrings.append(var)
        print(arrayOfStrings)
        return arrayOfStrings

    def conditions(self, val):
        if val == 2:
                # print("FACE ID : " + str(i) + " UN-ATTENTIVE WITH YAWNING")
            return "UN-ATTENTIVE WITH YAWNING"
        elif val == 1:
            # print("FACE ID : " + str(i) + " UN-ATTENTIVE WITH EYES CLOSED")
            return "UN-ATTENTIVE WITH EYES CLOSED"
        else:
            # print("UNDETECTED")
            return "UNDETECTED"

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
