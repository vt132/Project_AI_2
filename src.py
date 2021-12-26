from math import ceil
from pysat.formula import CNF
from pysat.solvers import Solver, Minisat22
import numpy

def cnflv1(queens):
    if((queens[0]-1)%8 != 0 or (queens[1]-1)%8 != 1 or (queens[2]-1)%8 != 2 or (queens[3]-1)%8 != 3 or (queens[4]-1)%8 != 4 or (queens[5]-1)%8 != 5 or (queens[6]-1)%8 != 6 or (queens[7]-1)%8 != 7):
        return None
    result = []
    #for prob d
    """
    for i in range(8):
        a = []
        for j in range(8):
            a.append(8*i+j+1)
        result.append(a)
    for i in range(1, 65):
        row = ceil(i/8)
        for j in range(i, row*8+1):
            if j == i:
                continue
            result.append([-i,-j])
    for i in range(1, 65):
        row = ceil(i/8)
        for j in range(i, 65, 8):
            if j == i:
                continue
            result.append([-i,-j])
    for i in range(1, 65):
        row = ceil(i/8)
        col = i % 8

        if col == 0:
            col = 8
        for j in range(i,min(((8- col + row)* 8 + 1)),65, 9):
            if j == i:
                continue
            result.append([-i, -j])
    for i in range(1, 65):
        for j in range(i, 65, 7):
            if i == j:
                continue
            elif ceil((j-7)/8) == ceil(j/8):
                break
            result.append([-i, -j])
    """
    for i in range(8):
        result.append([queens[i]])
        row = ceil(i/8)
        for j in range(i, row*8+1):
            if j==i:
                continue
            result.append([-j])
        for j in range(i, 65, 8):
            if j == i:
                continue
            result.append([-j])
        col = i % 8

        if col == 0:
            col = 8
        for j in range(i,min(((8- col + row)* 8 + 1)),65, 9):
            if j == i:
                continue
        result.append([-j])
        for j in range(i, 65, 7):
            if i == j:
                continue
            elif ceil((j-7)/8) == ceil(j/8):
                break
        result.append([-j])
    return result
def cnflv2(queens):
    result = []

    # for prob d
    """ 
    for i in range(8):
        a = []
        for j in range(8):
            a.append(8*i+j+1)
        result.append(a)
    for i in range(1, 65):
        row = ceil(i/8)
        for j in range(i, row*8+1):
            if j == i:
                continue
            result.append([-i,-j])
    for i in range(1, 65):
        row = ceil(i/8)
        for j in range(i, 65, 8):
            if j == i:
                continue
            result.append([-i,-j])
    for i in range(1, 65):
        row = ceil(i/8)
        col = i % 8

        if col == 0:
            col = 8
        for j in range(i,min(((8- col + row)* 8 + 1)),65, 9):
            if j == i:
                continue
            result.append([-i, -j])
    for i in range(1, 65):
        for j in range(i, 65, 7):
            if i == j:
                continue
            elif ceil((j-7)/8) == ceil(j/8):
                break
            result.append([-i, -j])
    """

    for i in range(8):
        result.append([queens[i]])
        row = ceil(i/8)
        for j in range(i, row*8+1):
            if j==i:
                continue
            result.append([-j])
        for j in range(i, 65, 8):
            if j == i:
                continue
            result.append([-j])
        col = i % 8
        if col == 0:
            col = 8
        for j in range(i,min(((8- col + row)* 8 + 1)),65, 9):
            if j == i:
                continue
        result.append([-j])
        for j in range(i, 65, 7):
            if i == j:
                continue
            elif ceil((j-7)/8) == ceil(j/8):
                break
        result.append([-j])
    return result

def solverlv1(queens):
    clauses=CNF()
    temp = cnflv1(queens)
    for i in temp:
        clauses.append(i)
    for i in range(8):
        a = []
        for j in range(8):
            a.append(8*i+j+1)
        clauses.append(a)
    for i in range(1, 65):
        row = ceil(i/8)
        for j in range(i, row*8+1):
            if j == i:
                continue
            clauses.append([-i,-j])
    for i in range(1, 65):
        row = ceil(i/8)
        for j in range(i, 65, 8):
            if j == i:
                continue
            clauses.append([-i,-j])
    for i in range(1, 65):
        row = ceil(i/8)
        col = i % 8

        if col == 0:
            col = 8
        for j in range(i,min(((8- col + row)* 8 + 1)),65, 9):
            if j == i:
                continue
            clauses.append([-i, -j])
    for i in range(1, 65):
        for j in range(i, 65, 7):
            if i == j:
                continue
            elif ceil((j-7)/8) == ceil(j/8):
                break
            clauses.append([-i, -j])

def solverlv2(queens):
    clauses=CNF()
    temp = cnflv1(queens)
    for i in temp:
        clauses.append(i)
    for i in range(8):
        a = []
        for j in range(8):
            a.append(8*i+j+1)
        clauses.append(a)
    for i in range(1, 65):
        row = ceil(i/8)
        for j in range(i, row*8+1):
            if j == i:
                continue
            clauses.append([-i,-j])
    for i in range(1, 65):
        row = ceil(i/8)
        for j in range(i, 65, 8):
            if j == i:
                continue
            clauses.append([-i,-j])
    for i in range(1, 65):
        row = ceil(i/8)
        col = i % 8

        if col == 0:
            col = 8
        for j in range(i,min(((8- col + row)* 8 + 1)),65, 9):
            if j == i:
                continue
            clauses.append([-i, -j])
    for i in range(1, 65):
        for j in range(i, 65, 7):
            if i == j:
                continue
            elif ceil((j-7)/8) == ceil(j/8):
                break
            clauses.append([-i, -j])
    with Minisat22(bootstrap_with=clauses) as m:
        m.solve()
