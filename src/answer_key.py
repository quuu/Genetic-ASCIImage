#!/usr/bin/env python3
import os
from skimage import io
from skimage import color
from PIL import Image

#TODO Multi-thread

def avg_brightness(image_list): 
    """
    A list of grey scale images
    """
    brightness_per_block=[]
    for image in image_list: 
        img_shape = image.shape
        img_Size = image.size
        total=0
        for i in range(0,img_shape[0]):
            for j in range(0,img_shape[1]):
              total+=image[i][j]  
        total/=img_Size
        brightness_per_block.append(total)
    return brightness_per_block

def make_image_list(image_paths):
    images = []
    for image in image_paths:
        colorImg = io.imread(image)
        greyImg = color.rgb2grey(colorImg)
        images.append(greyImg)
    return images

def my_crop(input, height, width, k, page):
    image_list = []
    im = Image.open(input)
    imgwidth, imgheight = im.size
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            a.save("IMG-%d.png"%k)
            image_list.append("IMG-%d.png"%k)
            k +=1
    return image_list

image_list = my_crop("picture.jpg",80,80,(220*220)/(80*80),"page_name")
images = make_image_list(image_list)
bright_per_block = avg_brightness(images)
print(bright_per_block)
