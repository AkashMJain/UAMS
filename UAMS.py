from imutils.video import FileVideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import CNNOperation as cnn
import MathematicalCalculationDLIB as mdl


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
            frame = self.cnn_op.CNNOperation(self.frame, self.net, self.args)
            cv2.imshow("frame", frame)
            fps.update()
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        fps.stop()
        print("elapsed time : {:.2f}".format(fps.elapsed()))
        print("FPS  : {:.2f}".format(fps.fps()))
        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

    def __init__(self):
        super(UAMS, self).__init__()
        self.argument_init()
        self.net = cv2.dnn.readNetFromCaffe(self.args["prototxt"], self.args["weights"])
        self.cnn_op = cnn.CNNOperation()

        self.UAMS()

        # print("\nJello")


UAMS()
