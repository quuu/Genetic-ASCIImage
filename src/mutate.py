
import picture


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


