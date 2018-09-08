#!/usr/bin/env python3
import sys
import os
import numpy as np
from skimage import io
import compare
import mutate
import generate_key as key
import generate_population as pop


if __name__ =="__main__":
    path = sys.argv[1]
    image = key.generate(path)

    # using the base image as a starting point for how big images should be
    width = image.get_width()
    height = image.get_height()
    population = pop.generate_pop(10,width,height)


'''
    for i in range(100):
        best_pop = compare.compare(image,population)
        a = mutate.offspring(0.01,best_pop[0],best_pop[1])

        '''
