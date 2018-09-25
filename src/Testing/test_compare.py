#!/usr/bin/env python3

import compare
import picture

testpic = ['*', ' ', '+', ' ', ' ', ' ', '*', '#', '#', '#']
target = picture.Picture(testpic, 5)

Population = []

testpic = ['*', '-', '+', ' ', ' ', ' ', '*', '#', ',', '#']
Population.append(picture.Picture(testpic, 5))
testpic = ['*', ' ', '+', ' ', ' ', ' ', '*', '#', '#', '#']
Population.append(picture.Picture(testpic, 5))
testpic = ['*', ' ', ' ', '.', ' ', ' ', '*', '#', '#', '#']
Population.append(picture.Picture(testpic, 5))
testpic = ['*', ' ', '+', ' ', ' ', '#', '*', '#', ' ', '#']
Population.append(picture.Picture(testpic, 5))
testpic = ['*', ' ', '+', ' ', '*', ' ', '*', '#', '#', '#']

best = compare.compare(target, Population)

best[0].print_picture()
best[1].print_picture()
