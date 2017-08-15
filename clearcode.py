#!/usr/bin/env python
# encoding: utf-8
"""
:brief: Module containing solutions of ClearCode recruitment tasks.
:author: Michal Modlinski
:created: 15.02.2017
"""

# Task 1: The odds are even in this war of mine.
#
# The struggle between the odd and even soldiers has never been so fierce! Each battle will see even and odd soldiers
# thrown in together, all of them integers. The odd soldiers in the battlefield will fight using the 1 bits from their
# binary representation, while the even soldiers will fight using their 0 bits. If present in the battle, soldiers with
# the number 0 will be neutral, hence they will not be fighting for either side. But beware - there are also spies and
# saboteurs - each soldier that wears negative sign can have a negative effect on the battle’s result.
#
# You should return:
# - odds win - if the number of "1" from odd soldiers is larger than the number of "0" from even soldiers
# - evens win - if the number of "1" from odd soldiers is smaller than the number of "0" from even soldiers
# - tie - if there is an equal number of "1" and "0" or when the battlefield is completely empty.
#
# Please note that any prefix that might appear in the binary representation, e.g. 0b , should not be counted towards
# the battle. Examples:
#
# Calculation for a battlefield configuration [5, 3, 14]:
# - odds: 5 and 3 => 101 and 11 => four "1"
# - evens: 14 => 1110 => one "0"
# - result: odds win the battle by a score of 4-1
#
# Examples with negative integers:
# battle([21,-3,20]) => "evens win" // 10101-11 vs 10100, 3-2 vs 3
# battle([7,-3,-14,6]) => "odds win" // 111-11 vs -1110+110, 3-2 vs -1+1
# battle([23,-3, 32, -24]) => "tie" // 10111-11 vs 100000-11000, 4-2 vs 5-3


def war_of_mine(soldiers):
    """
    :brief: Function counting points of even and odd soldiers on battlefield and choosing who is the winner.
    :param soldiers: list: Soldiers represent by integers in decimal representation present on the battlefield.
    :return: str: Result of battle.
    """
    odds = 0
    evens = 0
    for sol in soldiers:
        sol = bin(sol).replace('0b', '')
        if sol == '0':
            continue
        # Counting points for evens.
        elif sol[-1] == '0' and sol[0] != "-":
            for bit in sol:
                if bit == '0':
                    evens += 1
        elif sol[-1] == '0' and sol[0] == "-":
            for bit in sol:
                if bit == '0':
                    evens -= 1
        # Counting points for odds.
        elif sol[-1] == '1' and sol[0] != "-":
            for bit in sol:
                if bit == '1':
                    odds += 1
        elif sol[-1] == '1' and sol[0] == "-":
            for bit in sol:
                if bit == '1':
                    odds -= 1
    if evens > odds:
        return 'evens win'
    elif evens < odds:
        return 'odds win'
    else:
        return 'tie'

# Example 1.
print(war_of_mine([21, -3, 20]))

# Task 2: Minimum effort.
#
# You are moving through difficult terrain. Your goal is to move from the top left corner of the map to the bottom
# right, without losing too much energy. There’s one more constraint: you can only move to the right and down. Each
# field you will move through will have a number assigned - this is the cost of travelling through that field. Save your
# energy and win the competition!
#
# How to solve this problem:
# Your program should accept as its first argument a path to a filename, which contains the description of one or more
# terrain. The first line will have the value of n (the size of the square matrix). This will be followed by n rows of
# the matrix (integer costs in these rows will be comma delimited). After the n rows, the pattern repeats. For each
# terrain definition, please create a separate line where you will output the minimum effort required to travel through
# the terrain.
#
# Example input:
# 2
# 4,6
# 2,8
# 3
# 1,2,3
# 4,5,6
# 7,8,9
#
# Example output:
# 14
# 21

# Solution of task 2 has a little modification - an input is not a path to a filename. Moreover, it is not an efficient
# algorithm, but only a brute force solution.


def minimum_effort(*args):
    """
    :brief: Function printing minimum effort required to travel through the array for every set of data.
    :param args: int: First parameter is size of square array that game is played on and following parameters are
    numbers assigned to fields of array - at first fields from row number 1, then row number 2, and so on. After first
    array is defined, the pattern can repeat for another arrays.
    :return: int: Minimum effort required to travel through the terrain.
    """
    if not args:
        return None
    args = list(args)
    size = args[0]
    fields = args[1: 1 + size**2]
    array = [fields[i: i + size] for i in xrange(0, len(fields), size)]
    paths = [[args[1], 0, 0]]
    counter = 0
    while counter < 2 * (size - 1):
        new_paths = []
        for path in paths:
            if path[1] < size - 1:
                new_effort_y = path[0] + array[path[1] + 1][path[2]]
                new_path_y = [new_effort_y, path[1] + 1, path[2]]
                new_paths.append(new_path_y)
            if path[2] < size - 1:
                new_effort_x = path[0] + array[path[1]][path[2] + 1]
                new_path_x = [new_effort_x, path[1], path[2] + 1]
                new_paths.append(new_path_x)
        counter += 1
        paths = new_paths
    min_effort = min([path[0] for path in paths])
    del args[0: 1 + size**2]
    print(min_effort)
    return minimum_effort(*args)

# Example 2.
minimum_effort(2, 4, 6, 2, 8, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9)
