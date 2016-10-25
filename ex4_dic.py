# -*- coding: utf-8 -*-

import random


if __name__ == '__main__':
    #task1
    solar_system = {"Mercury": 57.9,
           "Venus": 108.2,
           "Earth": 149.6,
           "Mars": 227.9,
           "Jupiter": 778.3,
           "Saturn": 1427.0,
           "Uranus": 2871.0,
           "Neptune": 4497.1
    }
    print "task1\n", solar_system

    #task2
    print "\ntask2"
    for planet, distance in solar_system.items():
        print "Планета {0} находится в {1} млн км от Солнца".format(planet, distance)

    print "\ntask3 (sorted by name)"
    for planet in sorted(solar_system):
        print "Планета {0} находится в {1} млн км от Солнца".format(planet, solar_system.get(planet))

    print "\ntask4 (sorted by distance)"
    solar_system_reverse = dict(zip((solar_system.values()), (solar_system.keys())))
    for distance in sorted(solar_system_reverse.keys()):
        print "Планета {0} находится в {1} млн км от Солнца".format(solar_system_reverse.get(distance), distance)

    print "\ntask5 random planet"
    random_key = solar_system.keys()[random.randint(0, 7)]
    print "Планета {0} находится в {1} млн км от Солнца".format(random_key, solar_system.get(random_key))