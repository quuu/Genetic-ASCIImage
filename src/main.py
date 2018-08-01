import os
import numpy as np
from skimage import io
import seed
import color




def run():
    print("Running")


if __name__ =="__main__":
    img = io.imread("picture.jpg")
    print(img.shape)
    a = seed.Seed(10)
    a.arr.append(10)
    print(a.hashIt())
    a = color.Color(10,10,10)
