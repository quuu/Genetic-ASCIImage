<<<<<<< HEAD
import numpy as np
=======
#!/usr/bin/env python3

:import numpy as np
import color
>>>>>>> master
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

    def arrayPrint(self):
        print(self.pixels)
    def averageValue(self):
        total=0.0
        for i in self.pixels:
            total+=i
        total = total/len(self.pixels)
        return total
