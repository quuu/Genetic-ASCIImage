#!/usr/bin/env python3
import sys
from breader import *
import argparse






if __name__ == "__main__":
    '''
    main loop to compare current generations and evolve

    best_pop = the 2 best images of population

    population = best_pop merged together with n mutation rate

    population = regenerated with mutations and the base DNA
    '''
 
    path = sys.argv[1]
    image = generate(path)
    
    image.print_picture()
    width = image.get_width()
    height = image.get_height()
    population = generate_pop(1000,image,width,height)

    mutation_rate = 0.50
    best_pop = None
    for i in range(2000):
        best_pop = compare(image,population)
        for j in best_pop:
            # j.print_picture()
            print(j.get_fitness(), " ====== ", (height*width)/2)
            if(j.get_fitness() > (height*width)/2):
                break

        population = generate_new_population(mutation_rate - 0.01, best_pop,50,image)

        

main()