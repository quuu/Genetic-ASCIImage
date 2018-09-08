import random
import picture
import bright


'''
generates new population given a max population, a mating pool of pictures, and the base image
'''
def generate_new_population(mating_pool, max_pop,Target):
    population=[]
    for i in range(max_pop):
        parent1 = mating_pool[random.randint(0,len(mating_pool)-1)]
        parent2 = mating_pool[random.randint(0,len(mating_pool)-1)]
        a = picture.Picture(parent1.get_rep()[:int(len(parent1.get_rep())/2)]+parent2.get_rep()[int(len(parent2.get_rep())/2):],parent1.get_width(),parent1.get_height(),Target)
        a = mutate(0.05,a)
        population.append(a)
    return population

'''
creates a single offspring from two picture objects
'''
def offspring(mutation_rate,picture1,picture2):
    width = picture1.get_width()
    height = picture1.get_height()
    a = picture.Picture(picture1.get_rep()[:int((height*width)/2):]+picture2.get_rep()[int((height*width)/2)::],width,height)
    return mutate(mutation_rate,a)


'''
function to alter random parts of the art based on a rate
adds diversity to the pool
'''
def mutate(mutation_rate,offspring):
    for i in range(len(offspring.get_rep())):
        if(random.randint(0,100) < mutation_rate * 100):
            if(offspring.get_rep()[i] != '\n'):
                offspring.mutated(offspring.get_rep()[:i]+ bright.ASCII_CHARS[random.randint(0,len(bright.ASCII_CHARS)-1)] + offspring.get_rep()[i+1:])
    return offspring


