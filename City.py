import numpy as np, random, operator
class City:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def distance(self, city):
        xDis = abs(self.__x - city.__x)
        yDis = abs(self.__y - city.__y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance

    def __repr__(self):
        return "(" + str(self.__x) + "," + str(self.__y) + ")"

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value