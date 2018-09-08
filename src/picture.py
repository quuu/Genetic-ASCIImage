#!/usr/bin/env python3
import compare
class Picture:
    """
    ASCII picture representation object
    """
    # takes in a 1d array and the amount of chars per row
    # like a 2d array represented in 1d space

    '''
    constructor that does calculate fitness
    if a target image is supplied
    '''
    def __init__(self, rep, width ,height,Target=None):
        self.rep = rep
        self.width = width
        self.height = height
        if(Target != None):
            if(Target.get_width() != width or Target.get_height() != height):
                print("sizes are not the same")
            else:
                self.fitness = compare.compute_fitness(Target, rep)

    # member function to print the picture
    def print_picture(self):
        print(self.rep)

    '''
    accessors
    '''
    def get_rep(self):
        return self.rep

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_fitness(self):
        return self.fitness

    '''
    modifier
    '''
    def mutated(self,rep):
        self.rep = rep
