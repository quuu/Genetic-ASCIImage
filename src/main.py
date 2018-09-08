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
    population = pop.generate_pop(100,image,width,height)

    '''
    main loop to compare current generations and evolve

    best_pop = the 2 best images of population

    population = best_pop merged together with n mutation rate

    population = regenerated with mutations and the base DNA
    '''

    best_pop = None
    for i in range(2000):
        best_pop = compare.compare(image,population)
        for j in best_pop:
            j.print_picture()
            print(j.get_fitness(), " ====== ",(height*width)/2)
            if(j.get_fitness() > (height*width)/2):
                break

        population = mutate.generate_new_population(best_pop,100,image)





