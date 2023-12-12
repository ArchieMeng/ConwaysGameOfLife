from os import urandom, system
from time import sleep

# 0 for a dead cell, 1 for a live cell
def genMat(l):
    m = [[int.from_bytes(urandom(1)) % 2 for _ in range(l)] for _ in range(l)]
    # wrapping with 0 so that no edge detection is needed while computing surrounding cells
    m[0] = m[-1] = [0] * l
    for row in m:
        row[0] = row[-1] = 0
    return m

def printMat(m):
    for row in m:
        print(row)

def populate(m):
    new_mat = [list(row) for row in m]
    for i, row in enumerate(m[1:-1]):
        for j, v in enumerate(row[1:-1]):
            n_alive = 0
            n_alive += m[i][j]
            n_alive += m[i][j + 1]
            n_alive += m[i][j + 2]
            n_alive += m[i + 1][j]
            n_alive += m[i + 1][j + 2]
            n_alive += m[i + 2][j]
            n_alive += m[i + 2][j + 1]
            n_alive += m[i + 2][j + 1]

            if v == 1:
                if n_alive < 2 or n_alive > 3:
                    new_mat[i + 1][j + 1] = 0
                else:
                    new_mat[i + 1][j + 1] = 1
            else:
                if n_alive == 3:
                    new_mat[i + 1][j + 1] = 1
    return new_mat


m = genMat(30)
printMat(m)

while True:
    m = populate(m)
    print()
    printMat(m)
    sleep(0.5)
    system("clear")
