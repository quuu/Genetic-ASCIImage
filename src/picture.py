'''
Array of ASCII chars object

'''


class Picture:

    # takes in a 1d array and the amount of chars per row
    # like a 2d array represented in 1d space
    def __init__(self,rep,charsPerRow):
        self.rep = rep
        self.charsPerRow = charsPerRow

    # member function to print the picture
    def printPicture(self):
        count =0
        for i in self.rep:
            if(count==self.charsPerRow):
                print("\n")
                count=0
            print(i, end='')
            count+=1
        print()

