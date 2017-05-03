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
# Import python libraries

import copy
from random import Random  # need this for the random number generation -- do not change
import numpy as np
import math

# to setup a random number generator, we will specify a "seed" value
# need this for the random number generation -- do not change
seed = 5113
myPRNG = Random(seed)

# to get a random number between 0 and 1, use this:             myPRNG.random()
# to get a random number between lwrBnd and upprBnd, use this:  myPRNG.uniform(lwrBnd,upprBnd)
# to get a random integer between lwrBnd and upprBnd, use this: myPRNG.randint(lwrBnd,upprBnd)

# number of elements in a solution
n = 100

mk = 100

# initial temperature
T = 5000.0

# stopping temperature
T_min = 1.0

# cooling schedule
alpha = 0.95


# create an "instance" for the knapsack problem
value = []
for i in range(0, n):
    value.append(myPRNG.uniform(10, 100))

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
    b = np.array(value)
    c = np.array(weights)

    totalValue = np.dot(a, b)  # compute the value of the knapsack selection
    totalWeight = np.dot(a, c)  # compute the weight value of the knapsack selection

    if totalWeight > maxWeight:
        totalValue = maxWeight - totalWeight
    return [totalValue, totalWeight]  # returns a list of both total value and total weight


# 1-flip neighborhood of solution x
def neighborhood(x):
    nbrhood = []

    for i in range(0, n):
        nbrhood.append(x[:])
        if nbrhood[i][i] == 1:
            nbrhood[i][i] = 0
        else:
            nbrhood[i][i] = 1
    return nbrhood


# Create initial solution
def initial_solution():
    x = []

    for i in range(0, n):
        x.append(myPRNG.randint(0,1))
    return x


def acceptance_probability(old_cost, new_cost, T):
    ap = math.exp((evaluate(s)[0] - f_best)/T)
    return ap

# variable to record the number of solutions evaluated
solutionsChecked = 0

x_curr = initial_solution()  # x_curr will hold the current solution
x_best = x_curr[:]  # x_best will hold the best solution
f_curr = evaluate(x_curr)[0]  # f_curr will hold the evaluation of the current solution
f_best = f_curr

totalWeight = evaluate(x_curr)[1]


# begin Simulated Annealing ----------------
done = 0

while done == 0:
    m = 0

    while m < mk:

        Neighborhood = neighborhood(x_curr)  # create a list of all neighbors in the neighborhood of x_curr
        s = Neighborhood[myPRNG.randint(0, len(Neighborhood)-1)]  # Select a random neighbor from the neighborhood of x_curr

        solutionsChecked = solutionsChecked + 1

        if evaluate(s)[0] > f_best:
            x_best = s[:]  # find the best member and keep track of that solution
            f_best = evaluate(s)[0]  # and store its evaluation
            totalWeight = evaluate(s)[1]

        else:
            ap = acceptance_probability(evaluate(s)[0], f_best, T)
            if ap > myPRNG.random():
                x_best = s[:]
                f_best = evaluate(s)[0]
                totalWeight = evaluate(s)[1]


        m = m + 1


    T = alpha * T


    if T < T_min:
        done = 1

    else:
        x_curr = x_best[:]
        f_curr = f_best

        print("\nTotal number of solutions checked: ", solutionsChecked)
        print("Best value found so far: ", f_best)
        print("Current solution: ", x_curr)
        print("\nCurrent Temp: ", T)

print("\nFinal number of solutions checked: ", solutionsChecked)
print("Best value found: ", f_best)
print("Weight is: ", totalWeight)
print("Total number of items selected: ", np.sum(x_best))
print("Best solution: ", x_best)
