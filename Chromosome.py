from random import randint, random, sample


def generateNewValue(lim1, lim2):
    return randint(lim1, lim2)


class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.__repres = sample(range(0, len(problParam['cityList'])), len(problParam['cityList']))
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        r1 = randint(1, len(self.__repres) - 1)
        r2 = randint(r1, len(self.__repres))
        newrepres1 = []
        for i in range(len(self.__repres)):
            if i in range(r1, r2):
                newrepres1.append(self.repres[i])
        newrepres2 = [item for item in c.repres if item not in newrepres1]
        newrepres = newrepres1 + newrepres2
        offspring = Chromosome(c.__problParam)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        for swapped in range(len(self.__repres)):
            if random() < self.__problParam['mutationRate']:
                swapWith = int(random() * len(self.__repres))
                city1 = self.__repres[swapped]
                city2 = self.__repres[swapWith]
                self.__repres[swapped] = city2
                self.__repres[swapWith] = city1

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
