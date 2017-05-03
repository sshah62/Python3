# Sanjiv Shah | OU ID: 113180542
# DSA 5113, Spring 2017, Homework 4, Problem 6 (Simulated Annealing)

# basic hill climbing search provided as base code for the DSA/ISE 5113 course
# author: Charles Nicholson
# date: 4/5/2017

# NOTE: YOU MAY CHANGE ALMOST ANYTHING YOU LIKE IN THIS CODE.
# However, I would like all students to have the same problem instance, therefore please do not change anything relating to:
#   random number generation
#   number of items (should be 100)
#   random problem instance
#   weight limit of the knapsack

# ------------------------------------------------------------------------------

# need some python libraries

import copy
from random import Random  # need this for the random number generation -- do not change
import numpy as np

# to setup a random number generator, we will specify a "seed" value
# need this for the random number generation -- do not change
seed = 5113
myPRNG = Random(seed)

# to get a random number between 0 and 1, use this:             myPRNG.random()
# to get a random number between lwrBnd and upprBnd, use this:  myPRNG.uniform(lwrBnd,upprBnd)
# to get a random integer between lwrBnd and upprBnd, use this: myPRNG.randint(lwrBnd,upprBnd)

# number of elements in a solution
n = 100

# tabu tenure
tenure = 10

# maximum number of iterations
max_iterations = 1000

# create an "instance" for the knapsack problem
values = []
for i in range(0, n):
    values.append(myPRNG.uniform(10, 100))


weights = []
for i in range(0, n):
    weights.append(myPRNG.uniform(5, 20))

# define max weight for the knapsack
maxWeight = 5 * n

# change anything you like below this line ------------------------------------

# monitor the number of solutions evaluated
solutionsChecked = 0

# function to evaluate a solution x
def evaluate(x):
    a = np.array(x)
    b = np.array(values)
    c = np.array(weights)

    totalValue = np.dot(a, b)  # compute the value of the knapsack selection
    totalWeight = np.dot(a, c)  # compute the weight value of the knapsack selection

    if totalWeight > maxWeight:
        totalValue = maxWeight - totalWeight
    return [totalValue, totalWeight]


# here is a simple function to create a neighborhood
# Define 1-flip neighborhood 
def neighborhood(x):
    nbrhood = []
    for i in range(0, n):
        nbrhood.append(x[:])
        if nbrhood[i][i] == 1:
            nbrhood[i][i] = 0
        else:
            nbrhood[i][i] = 1
    return nbrhood


# create the initial solution
def initial_solution():
    x = []
    for i in range(0, n):
        x.append(myPRNG.randint(0,1))
    return x


# variable to record the number of solutions evaluated
solutionsChecked = 0

x_curr = initial_solution()  # x_curr will hold the current solution
x_best = x_curr[:]  # x_best will hold the best solution
f_curr = evaluate(x_curr)[0]  # f_curr will hold the evaluation of the current solution
totalWeight = evaluate(x_curr)[1]
f_best = f_curr

tabuList = {}

for i in range(max_iterations):

    Neighborhood = neighborhood(x_curr)  # create a list of all neighbors in the neighborhood of x_curr

    x_neighbor = Neighborhood[0]
    f_neighbor = evaluate(x_neighbor)[0]
    totalWeightNeighbor = evaluate(x_neighbor)[1]

    for s in Neighborhood:  # evaluate every member in the neighborhood of x_curr
        solutionsChecked = solutionsChecked + 1

        if evaluate(s)[0] > f_neighbor:
            index = abs(np.array(s) - np.array(x_curr)).argmax()
            if index in tabuList:
                if evaluate(s)[0] > f_best:
                    x_neighbor = s[:]
                    f_neighbor = evaluate(s)[0]
                    totalWeightNeighbor = evaluate(s)[1]
            else:
                x_neighbor = s[:]
                f_neighbor = evaluate(s)[0]
                totalWeightNeighbor = evaluate(s)[1]


    previous_x_curr = x_curr
    x_curr = x_neighbor


    if f_neighbor > f_best:
        x_best = x_neighbor
        f_best = f_neighbor
        totalWeight = totalWeightNeighbor

    # update
    previousList = tabuList
    tabuList = {}

    for key, value in previousList.items():
        if value > 1:
            tabuList[key] = value - 1


    index = abs(np.array(x_curr) - np.array(previous_x_curr)).argmax()
    tabuList[index] = tenure

    print("\nTotal number of solutions checked: ", solutionsChecked)
    print("Best Value for this iteration: ", f_neighbor)
    print("Best value found so far: ", f_best)
    print("Current solution: ", x_curr)
    print("Total number of items selected: ", np.sum(x_curr))

print("\nFinal: Total number of solutions checked: ", solutionsChecked)
print("Best value found: ", f_best)
print("Weight of knapsack: ", totalWeight)
print("Best solution: ", x_best)