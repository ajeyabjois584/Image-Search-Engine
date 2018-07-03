import cv2
import numpy as np

class ColorDescriptor:

    def __init__(self, bins):
        self.bins = bins

    def describe(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []
        h, w = image.shape[:2]
        (cX, cY) = (int(w/2), int(h/2))

        # all co ordinates taken in fourth quadrant where 1st and 3rd value indicates starting (x,y) coordinate
        # and 2nd and 4th tuple indicates ending (x,y) coordinate

        segments = [(0, cX, 0, cY), (cX, w, 0, cY), (0, cX, cY, h), (cX, w, cY, h)]

        # for computing elliptical major and minor axis
        # radius is taken as 75% of width and height which includes from both sides

        (axesX, axesY) = (int(w*0.75/2), int(h*0.75/2))
        ellipmask = np.zeros(image.shape[:2], dtype = "uint8")

        cv2.ellipse(img=image,center=(cX,cY), axes=(axesX,axesY), angle=0, startAngle=0, endAngle=360 , color=(255, 255, 255), thickness=-1)

        for startx, endx, starty, endy  in segments:

            # considers each of the top left,top right,bottom left,bottom right from image
            cornormask = np.zeros(image.shape[:2], dtype = "uint8")
            # draws rectangle over those regions specified above
            cv2.rectangle(cornormask, (startx,starty),(endx,endy),255,-1)
            # subtracts cornor square portions from elliptical to get region of intrest
            cornormask = cv2.subtract(cornormask,ellipmask)

            # extracting the color feature for the required mask and adding it to feature list
            hist = self.histogram(image,cornormask)
            features.extend(hist)

        # finally adding the color feature of central part and adding it to feature list
        hist = self.histogram(image,ellipmask)
        features.extend(hist)

        return features

    def histogram(self,image,mask):
        # to extract 3d histogram from required part of image passed as mask parameter
        hist = cv2.calcHist([image], [0,1,2], mask, self.bins, [0, 180, 0, 256, 0, 256])

        # we normalize the histogram so that it is not affected by scaling factor ie histogram remains same
        # for both 32x32 , 64x64, 128x128
        hist = cv2.normalize(hist,hist)
        hist = hist.flatten()


        return hist