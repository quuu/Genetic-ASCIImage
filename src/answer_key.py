#!/usr/bin/env python3
import os
from PIL import Image

def my_crop(input, height, width, k, page):
    im = Image.open(input)
    print(im)
    imgwidth, imgheight = im.size
    print(im.size)
    for i in range(0,imgheight,height):
        print(i)
        for j in range(0,imgwidth,width):
            print(j)
            box = (j, i, j+width, i+height)
            print(box)
            a = im.crop(box)
            print(a)
            a.save("IMG-%d.png"%k)
            k +=1

print("hellp")
my_crop("picture.jpg",80,80,(220*220)/(80*80),"page_name")