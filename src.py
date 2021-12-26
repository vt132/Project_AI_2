from math import ceil
from pysat.formula import CNF
from pysat.solvers import Solver, Lingeling
import numpy

def cnflv1(queens):
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
        if queens[i]==0 :
            break
        if queens[i]%8 != i:
            return []
        result.append([queens[i]])
        
        row = ceil(queens[i]/8)
        for j in range(row*8-7, row*8+1):
            if j==queens[i]:
                continue
            result.append([-j])
        col = queens[i] % 8
        if col == 0:
            col = 8
        for j in range(col, 65, 8):
            if j == queens[i]:
                continue
            result.append([-j])
        if(row-col < 0):
            uppermost_left = col
        else:
            uppermost_left = row*8
        for j in range(uppermost_left,min(((8- col + row)* 8 + 1),65), 9):
            if j == queens[i]:
                continue
            result.append([-j])
        uppermost_right = row + col
        for j in range(uppermost_right, 65, 7):
            if queens[i] == j:
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
        if queens[i]==0 :
            break
        result.append([queens[i]])
        
        row = ceil(queens[i]/8)
        for j in range(row*8-7, row*8+1):
            if j==queens[i]:
                continue
            result.append([-j])
        col = (queens[i]) % 8
        if col == 0:
            col = 8
        for j in range(col, 65, 8):
            if j == queens[i]:
                continue
            result.append([-j])
        if(row-col < 0):
            uppermost_left = abs(row-col) + 1
        else:
            uppermost_left = (row-col)*8+1
        for j in range(uppermost_left,min(((8- col + row)* 8 + 1),65), 9):
            if j == queens[i]:
                continue
            result.append([-j])
        if(row + col <= 9):
            uppermost_right = row + col - 1
        else:
            uppermost_right = (row-(8-col))*8 
        for j in range(uppermost_right, 65, 7):
            if queens[i] == j:
                continue
            elif ceil((j-7)/8) == ceil(j/8) and queens[i] < uppermost_right:
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
        for j in range(i,min(((8- col + row)* 8 + 1),65), 9):
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
    with Lingeling(bootstrap_with=clauses) as m:
        print(m.solve())
        print(m.get_core())

def solverlv2(queens):
    clauses=CNF()
    temp = cnflv2(queens)
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
        for j in range(i,min(((8- col + row)* 8 + 1),65), 9):
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
    print(clauses.clauses)
    with Lingeling(bootstrap_with=clauses.clauses, with_proof=True) as m:
        print(m.solve())
        print(m.get_proof())

def main():
    queens=[4, 15, 19, 32, 34, 45, 49, 62]
    solverlv2(queens)
main()