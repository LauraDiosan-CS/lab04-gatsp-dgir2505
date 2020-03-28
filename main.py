from City import City
from GA import GA


def readCiudat():
    cities = []
    cityRow = []
    cityList =[]
    with open(fileName_input, 'r') as f:
        N = None
        for i in range(0, 4):
            l = f.readline()
        li = [num for num in l.split(' ')]
        N=int(li[2])
        for i in range(0, 2):
            l = f.readline()
        for line in f:
            if line != 'EOF\n':
                values = [int(num) for num in line.split(' ')]
                cities.append(City(values[1], values[2]))
        for city1 in range(0, len(cities)):
            cityRow = []
            for city2 in range(0, len(cities)):
                distanta = cities[city1].distance(cities[city2])
                cityRow.append(distanta)
            cityList.append(cityRow)
        return N, cityList

def read():
    with open(fileName_input, 'r') as f:
        N = int(f.readline())
        cityList = [[int(num) for num in line.split(',')] for line in f]
    return N, cityList


def main():
    global fileName_input, N
    fileName_input = "50p_hard_01_tsp.txt"
    fileName_output = "50p_hard_01_tsp_solution.txt"

    N = None
    cityList=[]
    N, cityList=read()

    popSize = 100
    noGen = 1000
    mutationRate = 0.01
    eliteSize = 20
    ga = GA(popSize, eliteSize, cityList, mutationRate)
    ga.initialise()
    ga.evaluate()
    maximFitness = -1
    f = open(fileName_output, 'w')
    global currentChromosome
    for g in range(noGen):
        currentChromosome = ga.bestChromosome()
        if currentChromosome.fitness > maximFitness:
            maximFitness = currentChromosome.fitness
            bestChromo = currentChromosome
        # f.write('Best solution in generation ' + str(g) + ' is: x = ' + str(currentChromosome.repres) + ' f(x) = ' + str(currentChromosome.fitness))
        # f.write('\n')
        ga.oneGeneration()

    f.write(str(N))
    f.write('\n')
    index = 0
    for i in range(0, len(currentChromosome.repres)):
        if currentChromosome.repres[i] == 0:
            index = i
    i = index
    f.write(str(currentChromosome.repres[i] + 1) + ' ')
    i += 1
    while i != index:
        if i == len(currentChromosome.repres):
            i = 0
        else:
            f.write(str(currentChromosome.repres[i] + 1) + ' ')
            i += 1
    f.write('\n')
    route = currentChromosome.repres
    distance = 0
    for i in range(0, len(route)):
        fromCity = route[i]
        toCity = None
        if i + 1 < len(route):
            toCity = route[i + 1]
        else:
            toCity = route[0]
        distance += cityList[fromCity][toCity]
    f.write(str(distance))
    f.write('\n')
    f.close()


if __name__ == '__main__':
    main()
