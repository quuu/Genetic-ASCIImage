import numpy as np
'''
Class for each region of the image to be hashed

'''
class Seed:
    def __init__(self):
        self.pixels = []

    def newPixel(self,bright):
        self.pixels.append(bright)

    def printSeed(self):
        for i in self.pixels:
            print(i)

    def averageValue(self):
        total=0
        for i in self.pixels:
            total+=i
        total = total/len(self.pixels)
        return total
