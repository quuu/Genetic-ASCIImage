import picture
import random

ASCII_CHARS = ['.',',',':',';','+','*','?','S','$','#','@']
ASCII_CHARS = ASCII_CHARS[::-1]


def generate_picture(width,height):

    rep = []
    for i in range(height):
        for j in range(width):
            rep.append(ASCII_CHARS[random.randint(0,len(ASCII_CHARS)-1)])
        rep.append('\n')

    rep = ''.join(rep)
    return picture.Picture(rep,width,height)






def generate_pop(pop_size,width,height):
    population=[]
    for i in range(pop_size):
        population.append(generate_picture(width,height))
    return population

def testing():
    for i in ASCII_CHARS:
        print('i ------ '+str(ord(i)))
