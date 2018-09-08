import picture
import random

'''
the possible chars
'''


ASCII_CHARS = ['.',',',':',';','+','*','?','S','$','#','@']
ASCII_CHARS = ASCII_CHARS[::-1]

'''
generate an indidividual picture object
TODO:
    different way of generating initial population
    not completely random
'''

def generate_picture(width,height):

    rep = []
    for i in range(height):
        for j in range(width):
            '''
            easily expandable for more or less ASCII chars in the image
            '''
            rep.append(ASCII_CHARS[random.randint(0,len(ASCII_CHARS)-1)])
        if(i<height-1):
            rep.append('\n')
    rep = ''.join(rep)
    return picture.Picture(rep,width,height)



'''
method to be called
calls generate_picture the for the amount of population wanted
'''
def generate_pop(pop_size,width,height):
    population=[]
    for i in range(pop_size):
        population.append(generate_picture(width,height))
    return population

