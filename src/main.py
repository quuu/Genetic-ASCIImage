#!/usr/bin/env python3

import os
import numpy as np
from skimage import io
import seed
import picture
import answer_key as grey
import compare


def run():
    print("Running")


if __name__ =="__main__":

    img = io.imread("picture.jpg")
    picture_height = img.shape[0]
    picture_width = img.shape[1]

    # creates a list of greyscale values
    image_list = grey.my_crop("picture.jpg",10,10,(220*220)/(80*80),"page_name")
    images = grey.make_image_list(image_list)
    bright_per_block = grey.avg_brightness(images)

    seeds_per_row = picture_width/grey.cropped_dimensions(images)[0]
'''
    img = io.imread("picture.jpg")
    count=0

    # the percentage to scale the picture down to fit 80 pixels
    scaleFactorW=img.shape[0]/80
    scaleFactorH=img.shape[1]/(img.shape[1]/scaleFactorW)

    seedHeight = int(img.shape[0]/50)
    seedWidth= int(img.shape[1]/50)
    print(seedWidth)
    print(seedHeight)
    print(img.shape)

    rowCounter=0

    values=[]


    # loop for every pixel in height
    for i in range(img.shape[1]):

        if(count==0):
            for l in range(img.shape[1]):
                values.append(seed.Seed())

        elif(count==seedHeight):
            print(count,seedHeight)
            rowCounter+=1
            count=0

        # loop for every pixel in width
        for j in range(img.shape[0]):
            values[rowCounter*(int(i/seedWidth)-1)].newPixel(img[j][i][0]*0.2126 + img[j][i][1]*0.7152 + img[j][i][2]*0.0722)
        count+=1
    bright=[]
    # for the amount of rows in the image
    for i in range(img.shape[1]):

        # whenever the count returns, append row amount of seeds
        if(count==0):
            for l in range(int(img.shape[1])):
                values.append(seed.Seed())

        # if all the seeds in a certain region have been read
        # increment rowCounter so instead of looking at
        # indices 0-4, look at 5-8
        elif(count==seedHeight):
            print("row counter ++")
            rowCounter+=1
            count=0
        print(count)
        # read in pixel values
        for j in range(img.shape[0]):
        # red is i=0 in img[n][m][i] multiply by 0.2126
        # green is i=1 in img[n][m][i] multiply by 0.7152
        # blue is i=2 in img[n][m][i] multiply by 0.0722
            print("size ", len(values), " value ", rowCounter*int(j/seedWidth))
            values[rowCounter*(int(i/seedWidth)-1)].newPixel(img[j][i][0]*0.2126 + img[j][i][1]*0.7152 + img[j][i][2]*0.0722)
            #print("right side ", img[i][j]," i ", i, " j ", j)
            #print("inverted ", img[j][i], " i ", i, " j ", j)
        count+=1


    #test image
    testPic=['*',' ','+', ' ',' ',' ','*','#','#','#']
    obj= picture.Picture(testPic,5)

    obj.printPicture()
'''
