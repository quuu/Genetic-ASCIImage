#!/usr/bin/env python3
from breader import compute_fitness


class Picture:
    """
    ASCII picture representation object
    """
    def __init__(self, rep, height, width, target=None):
        self.rep = rep
        self.width = width
        self.height = height
        if target is not None:
            if target.get_width() != width or target.get_height() != height:
                print("sizes are not the same")
            else:
                self.fitness = compute_fitness(target, rep)

    def print_picture(self):
        '''

        :return:
        '''
        print(self.rep)

    def get_rep(self):
        '''

        :return:
        '''
        return self.rep

    def get_width(self):
        '''

        :return:
        '''
        return self.width

    def get_height(self):
        '''

        :return:
        '''
        return self.height

    def get_fitness(self):
        '''

        :return:
        '''
        return self.fitness

    def mutated(self,rep):
        '''

        :param rep:
        :return:
        '''
        self.rep = rep
