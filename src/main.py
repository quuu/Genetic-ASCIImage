#!/usr/bin/env python3

import os
import numpy as np
from skimage import io
import seed
import color
import picture



def run():
    print("Running")


if __name__ =="__main__":
    img = io.imread("picture.jpg")
    count=0
    seedWidth = int(img.shape[0]/50)
    seedHeight= int(img.shape[1]/50)
    print(seedWidth)
    print(seedHeight)
    print(img.shape)

    rowCounter=0

    values=[]
    # for every row in img
    for i in range(img.shape[1]):
        if(count==0):
            for i in range(int(img.shape[1]/seedWidth)):
                values.append([])
        # for every index in the row
        elif(count==seedHeight):
            rowCounter+=1
            count=0

        for j in range(img.shape[0]):
        # red is i=0 in img[n][m][i] multiply by 0.2126
        # green is i=1 in img[n][m][i] multiply by 0.7152
        # blue is i=2 in img[n][m][i] multiply by 0.0722
            j=j

    #test image
    testPic=['*',' ','+', ' ',' ',' ','*','#','#','#']
    obj= picture.Picture(testPic,5)

    obj.printPicture()
