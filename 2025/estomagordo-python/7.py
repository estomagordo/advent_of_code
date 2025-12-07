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
    sy = 0
    sx = 0

    while lines[sy][sx] != 'S':
        sx += 1

    return lines, sy, sx
    

def solve_a(lines):
    grid, sy, sx = parse(lines)
    h,w = dimensions(grid)
    splits = 0
    beams = {(sy, sx)}

    while beams:
        newbeams = set()

        for by, bx in beams:
            if by == h-1:
                continue

            if grid[by+1][bx] == '^':
                splits += 1
                newbeams.add((by+1, bx-1))
                newbeams.add((by+1, bx+1))
            else:
                newbeams.add((by+1,bx))

        beams = newbeams

    return splits


def solve_b(lines):
    grid, sy, sx = parse(lines)
    h,w = dimensions(grid)
    starts = {(sy, sx): 1}
    highest = 0
    timelines = 0

    while starts:
        new_starts = defaultdict(int)

        for pos, count in starts.items():
            by, bx = pos

            if by > highest:
                highest = by
                print(highest, h, len(starts))

            bdy = 1
            while by+bdy < h and grid[by+bdy][bx] != '^':
                bdy += 1

            if by+bdy < h and grid[by+bdy][bx] == '^':
                new_starts[(by+bdy,bx-1)] += count
                new_starts[(by+bdy,bx+1)] += count
            elif by+bdy >= h:
                timelines += count

        starts = new_starts

    return timelines


def main():
    lines = []

    with open('7.txt') as f:
        for line in f.readlines():
            lines.append(line)
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
