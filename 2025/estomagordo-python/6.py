from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, reduce
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, product
from math import ceil, comb, factorial, gcd, isclose, lcm
from operator import add, mul

from algo import a_star, custsort, merge_ranges, sssp
from constants import DIRECTIONS, EPSILON, HUGE, UNHUGE
from helpers import adjacent, between, chunks, chunks_with_overlap, columns, digits, dimensions, distance, distance_sq, eight_neighs, eight_neighs_bounded, find_in_grid, forward_rays_with_diagonals, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, overlap, positives, rays, rays_from_inside, solve_system, words


OPERATORS = {'+': add, '*': mul}

def parse(lines):
    raw_grid = [list(map(int, line.split())) for line in lines[:-1]]
    
    return [[raw_grid[y][x] for y in range(len(raw_grid))] + [OPERATORS[lines[-1].split()[x]]] for x in range(len(raw_grid[0]))]


def parse_b(lines):
    starts = [x for x in range(len(lines[-1])) if lines[-1][x] != ' ']
    widest = max(len(line) for line in lines)
    cols = []

    for colindex in range(len(starts)):
        stopx = starts[colindex+1] if colindex < len(starts) - 1 else widest
        startx = starts[colindex]
        operator = OPERATORS[lines[-1][startx]]
        col = []

        for x in range(stopx-1, startx-1, -1):
            num = ''

            for line in lines:
                if x < len(line) and line[x].isdigit():
                    num += line[x]

            if num:
                col.append(int(num))

        col.append(operator)
        cols.append(col)

    return cols
    

def solve_a(lines):
    cols = parse(lines)

    return sum(reduce(col[-1], col[:-1]) for col in cols)


def solve_b(lines):
    cols = parse_b(lines)

    return sum(reduce(col[-1], col[:-1]) for col in cols)


def main():
    lines = []

    with open('6.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())