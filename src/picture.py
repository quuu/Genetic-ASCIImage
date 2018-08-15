#!/usr/bin/env python3

class Picture:
    """
    ASCII picture representation object
    """
    # takes in a 1d array and the amount of chars per row
    # like a 2d array represented in 1d space
    def __init__(self, rep, chars_per_row):
        self.rep = rep
        self.chars_per_row = chars_per_row

    # member function to print the picture
    def print_picture(self):
        count =0
        for i in self.rep:
            if count==self.chars_per_row:
                print("\n")
                count=0
            print(i, end='')
            count+=1
        print()

    def get_rep(self):
        return self.rep


