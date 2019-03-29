# from imutils.video import FileVideoStream
# from imutils.video import FPS
from imutils import face_utils
from scipy.spatial import distance as dist

# import numpy as np
# import argparse
# import imutils
# import time
import cv2
import dlib


class MathematicalCalculationDLIB(object):
    """docstring for MathematicalCalculationDLIB"""

    def __init__(self):
        super(MathematicalCalculationDLIB, self).__init__()
        self.ctr = 0
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('./dlib_weights/shape_predictor_68_face_landmarks.dat')

        self.MOUTH_AR_CONSEC_FRAMES = 1
        self.EYE_AR_CONSEC_FRAMES = 1

        self.MOUTH_AR_THRESH = 0.09
        self.EYE_AR_THRESH = 0.3

        # self.YAWN = 0

        self.COUNTER_1 = 0
        self.COUNTER_2 = 0

        (self.lStart, self.lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (self.rStart, self.rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
        (self.mStart, self.mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
        (self.jStart, self.jEnd) = face_utils.FACIAL_LANDMARKS_IDXS["jaw"]
        (self.nStart, self.nEnd) = face_utils.FACIAL_LANDMARKS_IDXS["nose"]
        # self.arg = arg

    # def MathematicalCalculationDLIB(self):

    def faceMovement(self, leftEye, rightEye, nose):
        A = dist.euclidean(leftEye[0], nose[0])
        B = dist.euclidean(rightEye[3], nose[0])

        return A, B

    def eyeAspectRatio(self, eye):
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        C = dist.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)

        return ear

    def mouthAspectRatio(self, mouth):
        D1 = dist.euclidean(mouth[13], mouth[19])
        D2 = dist.euclidean(mouth[14], mouth[18])
        D3 = dist.euclidean(mouth[15], mouth[17])
        D4 = dist.euclidean(mouth[12], mouth[16])
        mar = (D1 + D2 + D3) / (3.0 * D4)

        return mar

    def loopOperation(self, frame):
        self.gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("test", self.gray)
        rects = self.detector(self.gray, 0)

        for rect in rects:
            self.shape = self.predictor(self.gray, rect)
            self.assignValues()
            self.calculateEAR()
            self.drawHullAndContours()
        if self.ctr == 0:
            print(rects)
            print("\n" + str(rect in rects))
            self.ctr = 1
        val = self.conditionChecking()
        return self.gray, val

    def assignValues(self):

        self.shape = face_utils.shape_to_np(self.shape)
        # eyes

        self.leftEye = self.shape[self.lStart:self.lEnd]
        self.rightEye = self.shape[self.rStart:self.rEnd]
        # Mouth
        self.mouth = self.shape[self.mStart:self.mEnd]
        # Nose
        self.nose = self.shape[self.nStart:self.nEnd]

    def calculateEAR(self):
        # eyes
        leftEAR = self.eyeAspectRatio(self.leftEye)
        rightEAR = self.eyeAspectRatio(self.rightEye)
        self.ear = (leftEAR + rightEAR) / 2.0

        # mouth
        self.mar = self.mouthAspectRatio(self.mouth)

        # Left Right Head Movements
        lef_dist, rig_dist = self.faceMovement(self.leftEye, self.rightEye, self.nose)

    def drawHullAndContours(self):
        mouthEyeHull = cv2.convexHull(self.mouth)
        leftEyeHull = cv2.convexHull(self.leftEye)
        rightEyeHull = cv2.convexHull(self.rightEye)
        cv2.drawContours(self.gray, [mouthEyeHull], -1, (0, 0, 255), 1)
        cv2.drawContours(self.gray, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(self.gray, [rightEyeHull], -1, (0, 255, 0), 1)

    def conditionChecking(self):

        if self.ear < self.EYE_AR_THRESH:
            return 1
        elif self.mar > self.MOUTH_AR_THRESH:
            return 2
        else:
            return 0

        # # print("in here")
        # if self.ear < self.EYE_AR_THRESH:
        #     self.COUNTER_1 += 1
        #     if self.COUNTER_1 >= self.EYE_AR_CONSEC_FRAMES:
        #         return 1
        #     cv2.putText(frame, "Eye Closing Detected!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        # else:
        #     self.COUNTER_1 = 0
        #     return 0

        # if self.mar > self.MOUTH_AR_THRESH:
        #     self.COUNTER_2 += 1
        #     if self.COUNTER_2 >= self.MOUTH_AR_CONSEC_FRAMES:
        #         return 2
        #     cv2.putText(frame, "Yawining Detected!", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # else:
        #     self.COUNTER_2 = 0
        #     return 0
