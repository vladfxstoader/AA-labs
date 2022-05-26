import math
import random
import copy

# Read data from input.txt.
def readData():
    global n, N, a, b, A, B, C, p, crossoverProb, mutationProb
    f = open("input.txt", "r")
    n = int(f.readline())
    a = float(f.readline())
    b = float(f.readline())
    A = float(f.readline())
    B = float(f.readline())
    C = float(f.readline())
    p = float(f.readline())
    crossoverProb = float(f.readline())
    mutationProb = float(f.readline())
    N = int(f.readline())

# Converts a list to a string by concatenating its elements.
def listToString(list):
    string = ""
    for element in list:
        string = string + str(element)
    return string

# Find necessary length for codification.
def getCodificationLength():
    global l
    l = int(math.log2((b - a) * 10**p)) + 1

# Generate l random genes for an individual.
def generateCromosoms():
    individual = []
    for i in range(l):
        individual.append(random.randint(0, 1))
    return individual

# Transform an individual (from base 2) to a number in base 10.
def base2to10(individual):
    pow = 1
    nr = 0
    for i in range(len(individual)-1, -1, -1):
        nr += pow*individual[i]
        pow *= 2
    nr = (b-a)/((2**l)-1)*nr + a
    return nr

# Calculate the fitness of an individual.
def fitness(individual):
    x = base2to10(individual)
    return A*(x**2) + B*x + C

# Applies f to a number.
def f(x):
    return A*(x**2) + B*x + C

# Generate genes for the entire initial population.
def generatePopulation():
    global population
    g.write("Initial population:\n")
    population = []
    for i in range(n):
        individual = generateCromosoms()
        population.append(individual)
        g.write(f"  {i}: {listToString(individual)} x = {base2to10(individual)} f = {fitness(individual)}\n")

# Binary search of a value in a list.
def search(list, x, left, right):
    if x <= list[left]:
        return left
    elif x >= list[right]:
        return right + 1
    elif left < right:
        mid = int((left + right)/2)
        if list[mid] <= x and list[mid+1] > x:
            return mid + 1
        elif list[mid] <= x and list[mid+1] <= x:
            return search(list, x, mid+2, right)
        else:
            return search(list, x, left, mid-1)

# Selection of the population.
def selection(population):
    global n, N, a, b, A, B, C, p, crossoverProb, mutationProb, bestFitness, selectionProb, y, maximumFitnessIndividual, fittest

    global intermediaryPopulation
    intermediaryPopulation = []
    intermediaryPopulationIndex = []
    F = 0 # sum of fitnesses of all individuals
    for i in range(len(population)):
        F += fitness(population[i])

    if y == 1:
        g.write("\nSelection probabilities:\n")

    # Selection probability for every individual.
    for i in range(len(population)):
        selectionProb.append(fitness(population[i])/F)
        if y == 1:
            g.write(f"  cromosome {i} probability {selectionProb[i]}\n")

    # Getting the individual with the maximum fitness.
    j = 1
    maximumFitness = 0
    maximumFitnessIndividualIndex = 0
    for i in range(len(population)):
        if fitness(population[i]) > maximumFitness:
            maximumFitness = fitness(population[i])
            maximumFitnessIndividualIndex = i
            maximumFitnessIndividual = copy.deepcopy(population[i])

    if maximumFitness > bestFitness:
        bestFitness = maximumFitness
        fittest = population[maximumFitnessIndividualIndex]

    fitValues.append(base2to10(fittest))

    if y == 1:
        g.write("\nSelection intervals:\n")

    # Getting the selection intervals.
    nr = 0
    intervals = []
    for i in range(0, n):
        selectionInterval = 0
        for k in range(0, i+1):
            selectionInterval += selectionProb[k]
        intervals.append(selectionInterval)
        if y == 1:
            nr = nr + 1
            g.write(f"  {intervals[i]} ")
            if nr == 3:
                g.write('\n')
                nr = 0

    if y == 1:
        g.write('\n\n')

    while j < n:
        x = random.uniform(0, 1)
        pos = search(intervals, x, 0, len(intervals)-1)
        if pos > len(population) - 1:
            pos = -1
        if y == 1:
            g.write(f"  u={x} select cromosome {pos}\n")
        if pos > len(intervals) - 1:
            pos = len(intervals) - 1
        intermediaryPopulationIndex.append(pos)
        j += 1

    # Generating the intermediary population.
    for index in intermediaryPopulationIndex:
        intermediaryPopulation.append((index, population[index]))

    if y == 1:
        g.write("\nAfter selection:\n")
        for index in intermediaryPopulationIndex:
            individual = population[index]
            if y == 1:
                g.write(f"  {index}: {listToString(individual)} x={base2to10(individual)} f={fitness(individual)}\n")

def crossover():
    global crossoverPopulation
    global witoutCrossover
    global crossoveredPopulation
    global populationAfterCrossover
    crossoverPopulation = []
    crossoveredPopulation = []
    witoutCrossover = []
    populationAfterCrossover = []

    if y == 1:
        g.write(f"\nCrossover probability {crossoverProb}\n")

    # Generating a random number in (0,1) and if it's
    # smaller than the crossover probability,
    # the individual will participate in the crossover.
    for individual in intermediaryPopulation:
        x = random.uniform(0, 1)
        if y == 1:
            g.write(f"  {individual[0]}: {listToString(individual[1])} u = {x}")
        if x < crossoverProb:
            crossoverPopulation.append(individual)
            if y == 1:
                g.write(" < 0.25 is participating")
        else:
            witoutCrossover.append(individual[1])
        if y == 1:
            g.write('\n')

    random.shuffle(crossoverPopulation)

    if y == 1:
        g.write('\n')
    i = 0
    while i < len(crossoverPopulation) - 1:
        firstIndividual = crossoverPopulation[i][1]
        secondIndividual = crossoverPopulation[i+1][1]
        firstIndividualIndex = crossoverPopulation[i][0]
        secondIndividualIndex = crossoverPopulation[i+1][0]

        crossoverPoint = random.randint(0, l)

        if y == 1:
            g.write(f"Crossover between cromosomes {firstIndividualIndex} and {secondIndividualIndex}:\n")
            g.write(f"{listToString(firstIndividual)} {listToString(secondIndividual)} crossover point {crossoverPoint}\n")

        firstPiece = firstIndividual[0:crossoverPoint]
        secondPiece = firstIndividual[crossoverPoint:]
        thirdPiece = secondIndividual[0:crossoverPoint]
        fourthPiece = secondIndividual[crossoverPoint:]

        crossoveredFirstIndividual = firstPiece + fourthPiece
        crossoveredSecondIndividual = secondPiece + thirdPiece

        list = [firstIndividual, secondIndividual, crossoveredFirstIndividual, crossoveredSecondIndividual]
        list = sorted(list, key = lambda x : fitness(x), reverse = True)

        crossoveredPopulation.append(list[0])
        crossoveredPopulation.append(list[1])

        if y == 1:
            g.write(f"  Result {listToString(crossoveredFirstIndividual)} {listToString(crossoveredSecondIndividual)}\n\n")

        i = i+2

    # Both the crossovered individuals and those who did not
    # participate in the crossover.
    for i in range(len(crossoveredPopulation)):
        populationAfterCrossover.append((i, crossoveredPopulation[i]))

    for i in range(len(witoutCrossover)):
        populationAfterCrossover.append((i+len(witoutCrossover), witoutCrossover[i]))

    if y == 1:
        g.write("After crossover:\n")
        for individual in populationAfterCrossover:
            g.write(f"  {individual[0]}: {listToString(individual[1])} x = {base2to10(individual[1])} f(x) = {fitness(individual[1])}\n")

def mutation():
    if y == 1:
        g.write(f"\nMutation probability for every gene {mutationProb}\n")
        g.write("The following cromosomes were modified:\n")

    # For each bit of each individual, a random number in (0,1) is generated.
    # If that number is smaller than the mutation probability, we negate that bit.
    for individual in populationAfterCrossover:
        for pos in range(len(individual[1])):
            x = random.uniform(0, 1)
            if x < mutationProb:
                individual[1][pos] = int(not(individual[1][pos]))
                if y == 1:
                    g.write(f"  {individual[0]}\n")
    if y == 1:
        g.write("After mutation:\n")
        for individual in populationAfterCrossover:
            g.write(f"  {individual[0]}: {listToString(individual[1])} x = {base2to10(individual[1])} f(x) = {fitness(individual[1])}\n")

def maximumEvolution():
    g.write("\nMaximum evolution:\n")
    values = [f(x) for x in fitValues]
    for value in values:
        g.write(f"{value}\n")

y = 0
# size of population
n = 0
# number of steps
N = 0
# endpoints of the interval
a = 0
b = 0
# coefficients of the function
A = 0
B = 0
C = 0
# precision
p = 0
crossoverProb = 0
mutationProb = 0
bestFitness = 0
fittest = []
l = 0
population = []
fitValues = []
populationAfterCrossover = []
maximumFitnessIndividual = []

g = open("evolution.txt", "w")
selectionProb = []
random.seed()
readData()
getCodificationLength()
generatePopulation()
y = 1
while y <= N:
    selection(population)
    crossover()
    mutation()
    population = []
    for individual in populationAfterCrossover:
        population.append(individual[1])
    population.append(maximumFitnessIndividual)
    y = y+1

maximumEvolution()





