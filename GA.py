import operator
from random import randint, random, sample

from Chromosome import Chromosome


def function(chromosome, cityList):
    route = chromosome.repres
    distance = 0
    for i in range(0, len(route)):
        fromCity = route[i]
        toCity = None
        if i + 1 < len(route):
            toCity = route[i + 1]
        else:
            toCity = route[0]
        distance += cityList[fromCity][toCity]
    return 1 / float(distance)*100


def rankFitness(population):
    results = {}
    for i in range(0, (len(population))):
        results[i] = population[i].fitness
    return sorted(results.items(), key=operator.itemgetter(1), reverse=True)


class GA:
    def __init__(self, size, eliteSize, cityList, mutationRate):
        self.__population = []
        self.__size = size
        self.__eliteSize = eliteSize
        self.__cityList = cityList
        self.__mutationRate = mutationRate

    @property
    def population(self):
        return self.__population

    def initialise(self):
        for _ in range(0, self.__size):
            problParam = {'cityList': self.__cityList, 'mutationRate': self.__mutationRate}
            c = Chromosome(problParam)
            self.__population.append(c)

    def evaluate(self):
        for c in self.__population:
            c.fitness = function(c, self.__cityList)

    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness < best.fitness:
                best = c
        return best

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness > best.fitness:
                best = c
        return best

    def selection(self):
        sortedPopulation = rankFitness(self.__population)
        selected = []
        for i in range(self.__eliteSize):
            selected.append(sortedPopulation[i][0])
        for i in range(0, len(sortedPopulation) - self.__eliteSize):
            pick = randint(0, self.__size-1)
            selected.append(pick)
        return selected

    def oneGeneration(self):
        newPop = []
        parents = []
        children = []
        selected = self.selection()
        for i in range(0, len(selected)):
            index = selected[i]
            parents.append(self.__population[index])

        randomParents = sample(parents, len(parents))
        for i in range(0, self.__eliteSize):
            children.append(parents[i])
        for i in range(0, len(parents) - self.__eliteSize):
            child = randomParents[i].crossover(randomParents[len(parents) - i - 1])
            children.append(child)

        for ind in range(0, len(children)):
            off = children[ind]
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluate()
