'''
Class for each pixel
'''

class Color:
    def __init__(self,red,green,blue):
        self.red = red
        self.green = green
        self.blue = blue
    def __str__(self):
        return "Red "+ str(self.red)+ " Blue "+ str(self.blue)+ " Green "+ str(self.green)
