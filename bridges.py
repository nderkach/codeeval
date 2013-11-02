#!/usr/bin/env python3
import sys
from collections import namedtuple, defaultdict
from itertools import product

"""
    Solution to codeeval.com Bay Area Bridge Challenge
    (https://www.codeeval.com/open_challenges/109/)
"""


def if_intersect(tup1, tup2):
    """ Check if two lines intersect
        Input: 2 tuples ([x1, y1], [x2, y2]) and ([x3, y3], [x4, y4])

    >>> if_intersect( ([1, 1], [3, 3]), ([2, 1], [1, 3]) )
    True
    >>> if_intersect( ([1, 1], [3, 3]), ([2, 1], [3, 2]) )
    False
    """

    Point = namedtuple('Point', 'x, y')
    p1a = Point(*tup1[0])
    p1b = Point(*tup1[1])
    p2a = Point(*tup2[0])
    p2b = Point(*tup2[1])

    # check if there are mutual abcisses
    if max(p1a.x, p1b.x) < min(p2a.x, p2b.x):
        return False

    a1 = (p1b.y-p1a.y)/(p1b.x-p1a.x)
    a2 = (p2b.y-p2a.y)/(p2b.x-p2a.x)
    b1 = p1a.y-a1*p1a.x
    b2 = p2a.y-a2*p2a.x

    # check if the lines are not parallel
    if (a1 == a2):
        return False

    # find the intersection and check if it belongs to the segment
    crosspoint = (b2-b1)/(a1-a2)
    return (max(min(p1a.x, p1b.x), min(p2a.x, p2b.x))
            < crosspoint <
            min(max(p1a.x, p1b.x), max(p2a.x, p2b.x)))

def get_no_of_intersections(bridges):
    """ Build a dictionary mapping bridge id to the bridge ids of all the bridges it intersects
    """
    no_of_intersections = defaultdict(list)
    for pr in product(bridges.keys(), repeat=2):
        if if_intersect(*pr):
            no_of_intersections[bridges[pr[0]]].append(bridges[pr[1]])
    return no_of_intersections

def build_bridges(bridges):
    """ Build all the bridges starting with those that have no no_of_intersections
        and then adding up those with intersections provided they don't
        intersect the built ones.
        To maximize the amount of bridges built, start with the ones
        that have the least amount of intersections
    """
    built_bridges = set()
    no_of_intersections = get_no_of_intersections(bridges)

    for bridgeid in bridges.values():
        if bridgeid not in no_of_intersections.keys():
            built_bridges.add(bridgeid)
    
    for bridgeid, intersected_bridges in sorted(no_of_intersections.items(), key=lambda x: len(x[1])):
        if not any([bridge for bridge in intersected_bridges if bridge in built_bridges]):
            built_bridges.add(bridgeid)

    for bridge in sorted(built_bridges):
        print(bridge)

if __name__=="__main__":
    bridges = {}
    with open(sys.argv[1]) as f:
        for line in f:
            bid, tup = line.strip().split(": ")
            bridges[tuple([tuple(c) for c in eval(tup)])] = int(bid)

    build_bridges(bridges)

    sys.exit(0)
