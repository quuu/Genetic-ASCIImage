import numpy as np
import color
'''
Class for each region of the image to be hashed

'''
class Seed:
    def __init__(self,size):
        self.width=size
        self.height=size
        self.arr = []

    # early hashing function, shoudl add all the greyscale values and then modulo to get the bin it belongs in
    def hashIt(self):
        n=0
        for i in self.arr:
           n+=i
        n*=100
        return n

