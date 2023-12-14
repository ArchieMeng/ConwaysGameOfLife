from os import urandom, system
from time import sleep
import pygame

# 0 for a dead cell, 1 for a live cell
def genMat(width, height):
    m = [[1 if int.from_bytes(urandom(1)) % 10 > 8 else 0 for _ in range(width)] for _ in range(height)]
    # wrapping with 0 so that no edge detection is needed while computing surrounding cells
    m[0] = m[-1] = [0] * width
    for row in m:
        row[0] = row[-1] = 0
    return m

def printMat(m):
    for row in m:
        print(row)

def addGlider(m, x, y):
    '''
    parameter m Mat to be added into
    parameter x: top-left x pos of glider
    parameter y: top-left y pos of glider
    '''
    gliderMat = [
            [1, 0, 0],
            [0, 1, 1],
            [1, 1, 0],
        ]
    for j, row in enumerate(gliderMat):
        for i, v in enumerate(row):
            m[y + j][x + i] = v


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
            n_alive += m[i + 2][j + 2]

            if v == 1:
                if n_alive < 2 or n_alive > 3:
                    new_mat[i + 1][j + 1] = 0
                else:
                    new_mat[i + 1][j + 1] = 1
            else:
                if n_alive == 3:
                    new_mat[i + 1][j + 1] = 1
    return new_mat

sz = 4
scr_w, scr_h = 1600, 900
m = genMat(scr_w // sz, scr_h // sz)
addGlider(m, 1, 1)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((scr_w, scr_h))
clock = pygame.time.Clock()
running = True

cnt = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    for i, row in enumerate(m):
        for j, v in enumerate(row):
            pygame.draw.circle(screen, "white" if v == 1 else "black", pygame.Vector2(j * sz, i * sz), sz // 2)

    cnt = (cnt + 1) % 10
    if cnt == 0:
        m = populate(m)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
