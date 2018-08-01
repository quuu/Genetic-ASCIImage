import os
import numpy as np
from skimage import io

if __name__ =="__main__":
    img = io.imread("picture.jpg")
    print(img.shape)