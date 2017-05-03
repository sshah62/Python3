# Sanjiv Shah | OU ID: 113180542
# DSA 5113, Spring 2017, Homework 4, Problem 7 (VNS)

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

# Evaluation function
def evaluate(x):
    a = np.array(x)
    b = np.array(values)
    c = np.array(weights)

    totalValue = np.dot(a, b)  # compute the value of the knapsack selection
    totalWeight = np.dot(a, c)  # compute the weight value of the knapsack selection

    if totalWeight > maxWeight:
        totalValue = maxWeight - totalWeight
    return [totalValue, totalWeight]  # returns a list of both total value and total weight

# Define neighborhood (1-flip, 2-flip, 3-flip)

def neighborhood(x):
    if flip == 1:
        nbrhood = []

        for i in range(0, n):
            nbrhood.append(x[:])
            if nbrhood[i][i] == 1:
                nbrhood[i][i] = 0
            else:
                nbrhood[i][i] = 1
                # end
                # end

    elif flip == 2:
        nbrhood = []
        a = -1
        for i in range(0, n):
            for j in range(i, n):
                if i != j:
                    a += 1
                    nbrhood.append(x[:])

                    if nbrhood[a][i] == 1:
                        nbrhood[a][i] = 0
                    else:
                        nbrhood[a][i] = 1
                    # end

                    if nbrhood[a][j] == 1:
                        nbrhood[a][j] = 0
                    else:
                        nbrhood[a][j] = 1
                    # end
                # end
            # end
        # end
    else:
        nbrhood = []
        a = -1
        for i in range(0, n):
            for j in range(i, n):
                for k in range(j, n):
                    if i != j and i != k and j != k:
                        a += 1
                        nbrhood.append(x[:])

                        if nbrhood[a][i] == 1:
                            nbrhood[a][i] = 0
                        else:
                            nbrhood[a][i] = 1
                        # end

                        if nbrhood[a][j] == 1:
                            nbrhood[a][j] = 0
                        else:
                            nbrhood[a][j] = 1
                        # end

                        if nbrhood[a][k] == 1:
                            nbrhood[a][k] = 0
                        else:
                            nbrhood[a][k] = 1
                        # end
                    # end
                # end
            # end
        # end
    # end

    return nbrhood
# end

# create the initial random solution
def initial_solution():
    x = []
    for i in range(0, n):
        x.append(myPRNG.randint(0,1))
    return x

# Create Solutions Counter
solutionsChecked = 0
best = 0.0
x_curr = initial_solution()  # x_curr will hold the current solution
x_best = x_curr[:]  # x_best will hold the best solution
f_curr = evaluate(x_curr)  # f_curr will hold the evaluation of the current solution
f_best = f_curr[:]
totalWeight = evaluate(x_curr)[1]


# Variable Neighborhood Search (local search: best improvement)
flip = 1
max_flip = 3

while flip < max_flip +1:

    Neighborhood = neighborhood(x_curr)  # create a list of all neighbors in the neighborhood of x_curr
    for s in Neighborhood:  # evaluate every member in the neighborhood of x_curr
        solutionsChecked = solutionsChecked + 1
        if evaluate(s)[0] > f_best[0]:
            x_best = s[:]  # find the best member and keep track of that solution
            f_best = evaluate(s)[:]  # and store its evaluation
            totalWeight = evaluate(s)[1]
    if f_best == f_curr:  # if there were no improving solutions in the neighborhood
        flip += 1
    else:
        x_curr = x_best[:]  # else: move to the neighbor solution and continue
        f_curr = f_best[:]  # evaluate the current solution

        print("\nTotal number of solutions checked: ", solutionsChecked)
        print("Best value found so far: ", f_best[0])


print("\nTotal number of solutions checked: ", solutionsChecked)
print("Best value found: ", f_best[0])
print("Total Weight of the knapsack (max 500): ", totalWeight)
print("Total number of items selected: ", np.sum(x_best))
print("Best solution found: ", x_best)