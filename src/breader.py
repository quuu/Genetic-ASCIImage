from PIL import Image
import random
from picture import Picture

'''
possible chars for brightness
'''
ASCII_CHARS = ['.', ',', ':', ';', '+', '*', '?', 'S', '$', '#', '@']
ASCII_CHARS = ASCII_CHARS[::-1]

#!/usr/bin/env python3

class Breader:

    def __init__(self, target, mutation_rate, crossover, population_size, number_of_parents, population):
        self.tar = target
        self.mutation_rate = mutation_rate
        self.crossover = crossover
        self.population_size = population_size
        self.number_of_parents = number_of_parents
        self.population = population


    def compute_fitness(self, target, member):
        '''
        Compares Target image to a member of the population
        :param target:Target image
        :type target:
        :param member: Member of population
        :return: number of coreect
        :rtype: int
        '''

        target_rep = target.get_rep()
        correct = 0
        if len(target_rep) != len(member):
            print("Error: Images must be of the same size")
        else:
            for x in range(0, len(target_rep)):
                if target_rep[x] == member[x]:
                    correct += 1
        return correct


    def compare(self, target, population):
        """
        This function takes in two picture objects and compares them.

        :param target: target image
        :type target: Picture object
        :param population: The population of the current generations
        :type population: A list of picture objects

        :return: Two best members of the population
        :rtype: A list of picture objects
        """

        target_rep = target.get_rep()
        target_len = len(target_rep)
        best_pop = []
        correctness_list = []
        for member in population:
            correct = 0
            member_rep = member.get_rep()
            if target_len != len(member_rep):
                print("Error: Images must be of the same size")
            else:
                for x in range(0, len(target_rep)):
                    if target_rep[x] == member_rep[x]:
                        correct += 1
            correctness_list.append(correct)

        for i in range(1):
            best_idx = correctness_list.index(max(correctness_list))
            best_pop.append(population[best_idx])
            del correctness_list[best_idx]
        return best_pop


    def generate(self, path):
        '''
        TODO add description

        :param path:
        :return:
        '''
        image = None
        try:
            image = Image.open(path)
        except Exception:
            print("Unable to find image in", path)
            return

        '''
        resizing the image
        '''

        (old_width,old_height) = image.size
        aspect_ratio = float(old_height)/float(old_width)
        new_width = 100
        new_height=int(aspect_ratio * new_width)
        new_dimensions = (new_width,new_height)
        image = image.resize(new_dimensions)

        '''
        grey scale the image
        '''

        image = image.convert('L')

        '''
        converting the image into ASCII representation based on
        brightness value of the pixel
        '''

        initial_pixels = list(image.getdata())
        new_pixels = [ASCII_CHARS[pixel_value//25] for pixel_value in initial_pixels]
        pixels = ''.join(new_pixels)

        '''
        inserting \n's to the ASCII for new lines of pixels
        '''

        size = len(pixels)
        new_image = [pixels[index:index+new_width] for index in range(0,size,new_width)]
        height= len(new_image)
        image = '\n'.join(new_image)


        '''
        making sure the image is good
        '''
        #print(image)

        '''
        uncomment this for actual implementation
        '''

        image = Picture(image,new_width,height)
        return image


    def generate_picture(self, target, width, height):


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
        return Picture(rep, width, height, target)


    def generate_pop(self, pop_size, target, width, height):
        '''

        :param pop_size:
        :param target:
        :param width:
        :param height:
        :return:
        '''
        population=[]
        for i in range(pop_size):
            population.append(generate_picture(target, width, height))
        return population

    def make_child(self, pic1, pic2):
        '''

        :param pic1:
        :param pic2:
        :return:
        '''

        pic1 = pic1.get_rep()
        pic2 = pic2.get_rep()

        child= []
        width = pic1.get_width()
        height = pic1.get_height()

        for i in range(0, width * height):
            r = random.randint(0,1)
            if r == 1:
                child.append(pic1[i])
            else:
                child.append(pic2[i])

        child = picture.Picture(child,width,height)
        return child



    def generate_new_population(self, mutation_rate, mating_pool, max_pop, target):
        '''
        generates new population given a max population, a mating pool of pictures, and the base image

        :param mutation_rate:
        :param mating_pool:
        :param max_pop:
        :param target:
        :return:
        '''

        population=[]
        for i in range(max_pop):
            parent1 = mating_pool[random.randint(0, len(mating_pool)-1)]
            parent2 = mating_pool[random.randint(0, len(mating_pool)-1)]
            a = picture.Picture(parent1.get_rep()[:int(len(parent1.get_rep())/2)]+parent2.get_rep()[int(len(parent2.get_rep())/2):], parent1.get_width(), parent1.get_height(), target)
            a = mutate(mutation_rate, a)
            population.append(a)
        return population


    def offspring(self, mutation_rate, picture1, picture2):
        '''

        :param mutation_rate:
        :param picture1:
        :param picture2:
        :return:
        '''
        #TODO: check to see if pic 1 and 2 have the same height and width
        '''
        creates a single offspring from two picture objects
        '''
        width = picture1.get_width()
        height = picture1.get_height()
        '''
        Simply splicing 2 images into 1
        '''
        #child = picture.Picture(picture1.get_rep()[:int((height*width)/2):]+picture2.get_rep()[int((height*width)/2)::],width,height)
        child = make_child(picture1, picture2)
        return mutate(mutation_rate, child)



    def mutate(self, mutation_rate,offspring):
        '''

        :param mutation_rate:
        :param offspring:
        :return:
        '''
        '''
        function to alter random parts of the art based on a rate
        adds diversity to the pool
        '''

        rep = offspring.get_rep()
        for i in range(len(offspring.get_rep())):
            if(random.randint(0,100) < mutation_rate * 100):
                if(rep[i] != '\n'):
                    offspring.mutated(rep[:i]+ ASCII_CHARS[random.randint(0,len(ASCII_CHARS)-1)] + offspring.get_rep()[i+1:])
        return offspring



