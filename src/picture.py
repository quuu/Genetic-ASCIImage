#!/usr/bin/env python3

class Picture:
    """
    ASCII picture representation object
    """
    # takes in a 1d array and the amount of chars per row
    # like a 2d array represented in 1d space
    def __init__(self, rep, width ,height):
        self.rep = rep
        self.width = width
        self.height = height

    # member function to print the picture
    def print_picture(self):
        print(self.rep)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


