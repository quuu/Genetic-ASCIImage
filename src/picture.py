#!/usr/bin/env python3
import compare
class Picture:
    """
    ASCII picture representation object
    """
    # takes in a 1d array and the amount of chars per row
    # like a 2d array represented in 1d space

    '''
    constructor that doesn't calculate fitness
    '''
    def __init__(self, rep, width, height):
        self.rep = rep
        self.width = width
        self.height = height

    '''
    constructor that does calculate fitness
    '''
    def __init__(self, rep, width ,height,Target):
        self.rep = rep
        self.width = width
        self.height = height
        if(Target.get_width() != width or Target.get_height() != height):
            print("sizes are not the same")
        else:
            self.fitness = compare.compute_fitness(Target, rep)

    # member function to print the picture
    def print_picture(self):
        print(self.rep)

    def get_rep(self):
        return self.rep

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


