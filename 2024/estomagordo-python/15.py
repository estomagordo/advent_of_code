from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, reduce
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, product
from math import ceil, comb, factorial, gcd, isclose, lcm

from algo import a_star, custsort, merge_ranges, sssp
from constants import DIRECTIONS, EPSILON, HUGE, UNHUGE
from helpers import adjacent, between, chunks, chunks_with_overlap, columns, digits, dimensions, distance, distance_sq, eight_neighs, eight_neighs_bounded, find_in_grid, forward_rays_with_diagonals, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, overlap, positives, rays, rays_from_inside, solve_system, words


def parse(lines):
    a, b = grouped_lines(lines)
    grid = []
    instructions = ''.join(line.rstrip() for line in b)

    for line in a:
        grid.append(list(line.rstrip()))
    
    return grid, instructions
    

def solve_a(lines):
    grid, instructions = parse(lines)
    height, width = dimensions(grid)

    y, x = find_in_grid(grid, '@')
    grid[y][x] = '.'

    for instruction in instructions:
        dy, dx = DIRECTIONS[instruction]

        next_cell = grid[y+dy][x+dx]

        match next_cell:
            case '#':
                continue
            case '.':
                y += dy
                x += dx
            case 'O':
                step = 1

                while grid[y+dy*step][x+dx*step] == 'O':
                    step += 1

                if grid[y+dy*step][x+dx*step] == '#':
                    continue

                grid[y+dy*step][x+dx*step] = 'O'
                grid[y+dy][x+dx] = '.'
                y += dy
                x += dx

    return sum(100 * y + x for y, x in product(range(height), range(width)) if grid[y][x] == 'O')


def solve_b(lines):
    data = parse(lines)

    return None


def main():
    lines = []

    with open('15.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
