### Lecture 1. Introduction to Software Design
### Interfaces in Python. Introduction

import sys
from abc import ABC, abstractmethod
### Option 1: Duck Typing

### Coords interface:
###
###   Returns a list of components in form (componentName, componentValue)
###   get_components(self)


### Option 2: OOP interface
class ICoords:
    def get_components(self):
        raise NotImplementedError('ICoords::get_components() not implemented')

## ------------------------------------------------------------------------- ##
# Option 1: Duck-typed interface implemented
class SphericalCoords:
    def __init__(self, dst, polar, azmth):
        self.distance = dst
        self.polarAngle = polar
        self.azimuthAngle = azmth

    # Duck-typed interface implemented.
    def get_components(self):
        return [('distance', self.distance),
                ('polarAngle', self.polarAngle),
                ('azimuthAngle', self.azimuthAngle)
               ]


# Option 2: OOP interface implemented
class HorizontalCoords(ICoords):
    def __init__(self, alt, azmth):
        self.altitude = alt
        self.azimuth = azmth

    def get_components(self):
        return [('altitude', self.altitude), ('azimuth', self.azimuth)]


# Option 2: OOP interface not implemented
class HorizontalCoordsBroken(ICoords):
    def __init__(self, alt, azmth):
        self.altitude = alt
        self.azimuth = azmth

    ### get_components() from ICoords is not implemented!
    ### def get_components(self):
    ###     return [('altitude', self.altitude), (azimuth, self.azimuth)]


## Option 3: Abstract base class with ABCMeta & abstractmethod() approach
class CoordsBase(ABC):
    @abstractmethod
    def get_components(self): pass


class SphericalCoordinates(CoordsBase):
    def __init__(self, dst, polar, azmth):
        self.distance = dst
        self.polarAngle = polar
        self.azimuthAngle = azmth

    # ABC interface implemented.
    def get_components(self):
        return [('distance', self.distance),
                ('polarAngle', self.polarAngle),
                ('azimuthAngle', self.azimuthAngle)
                ]


class Meteor:
    __mass = 0
    __size = 0
    __coords = ICoords()

    def __init__(self, m, s, c):
        self.__mass = m
        self.__size = s
        self.__coords = c

    def get_mass(self):
        return self.__mass

    def get_coords(self):
        return self.__coords


if __name__ == "__main__":
    print("Interfaces in Python.")

    # OOP 1
    m1 = Meteor(10, 11, HorizontalCoords(111, 222))
    print(m1.get_mass())
    print(m1.get_coords().altitude)
    print(m1.get_coords().azimuth)
    coordinates = m1.get_coords()

    print(coordinates.get_components())                              # Law of Demetra is violated!

    # OOP 2
    try:
        m2 = Meteor(10, 11, HorizontalCoordsBroken(111, 222))
        print(m2.get_coords().get_components())                          # Law of Demetra is violated!
    except Exception:
        print("Exception got on accessing components.")

    # Duck typed
    m3 = Meteor(10, 11, SphericalCoords(10, 12, 33))
    print(m3.get_coords().get_components())

    # ABC base
    m3 = Meteor(10, 11, SphericalCoordinates(10, 12, 34))
    print(m3.get_coords().get_components())
    print("Printing coords using dynamic polymorphism.")

    coordsList = [HorizontalCoords(111, 222),  # Using ICoords
                  SphericalCoords(10, 12, 33),  # Using Duck Typing
                  SphericalCoords(10, 12, 34),  # ABC
                  HorizontalCoords(555, 777)]   # Using ICoords

    for coord in coordsList:
        print(coord.get_components())
