#!/usr/bin/env python3

from picture import Picture

def return_brightness(ascii_chr):
    """
    Takes in an ascii character and returns the appropriate brightness for that character

    :param ascii_chr: An ascii character
    :return: Brightness value
    """

    ascii_arry = [' ', '-', '+', '*', '#']
    idx = None
    try:
        idx =  ascii_arry.index(ascii_chr)
    except ValueError as e:
        print("Error: in return_brightness: {}".format(e))
    return idx * (100/(len(ascii_arry)-1))

'''
Takes in Target image to compare to
member represetation to compare with
'''
def compute_fitness(Target,member):
    target_rep = Target.get_rep()
    correct=0
    if(len(target_rep)!=len(member)):
        print("Error: Images must be of the same size")
    else:
        for x in range(0,len(target_rep)):
            if(target_rep[x] == member[x]):
                correct+=1
    return correct

def compare(Target, Population):
    """
    This function takes in two picture objects and compares them.

    :param Target: target image
    :type Target: Picture object
    :param Population: The population of the current generations
    :type Population: A list of picture objects

    :return: Two best members of the population
    :rtype: A list of picture objects
    """

    target_rep = Target.get_rep()
    target_len = len(target_rep)
    best_pop = []
    correctness_list = []
    for member in Population:
        correct = 0
        member_rep = member.get_rep()
        if target_len != len(member_rep):
            print("Error: Images must be of the same size")
        else:
            for x in range(0, len(target_rep)):
                if target_rep[x] == member_rep[x]:
                    correct += 1
        correctness_list.append(correct)

    for i in range(10):
        best_idx = correctness_list.index(max(correctness_list))
        best_pop.append(Population[best_idx])
        del correctness_list[best_idx]
    return best_pop
