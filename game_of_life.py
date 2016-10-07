import sys
import pygame
from patterns import random_pattern, glider_pattern
from screen import refresh_screen

#Options
columns, rows = 100, 50
cell_size = 10

def wrap_neighbour(neighbour):
    (c, r) = neighbour
    c = 0 if c == columns else c
    c = columns - 1 if c == -1 else c
    r = 0 if r == rows else r
    r = rows - 1 if r == -1 else r
    return (c, r)


def wrap_neighbours(neighbours):
    return [ wrap_neighbour(n) for n in neighbours]


# Finding Neighbours
def get_neighbours((c, r)):
    neighbours =  [(c - 1, r - 1), (c, r - 1), (c + 1, r - 1),
                   (c + 1, r),                 (c + 1, r + 1),
                   (c, r + 1), (c - 1, r + 1), (c - 1, r)]
    return wrap_neighbours(neighbours)

def get_live_neighbours(cells, (c, r)):
    neighbours = get_neighbours((c, r))
    return [val for val in neighbours if val in cells]

def get_dead_neighbours(cells, (c, r)):
    neighbours = get_neighbours((c, r))
    return [val for val in neighbours if val not in cells]


# Living And Dying
def surviving(cells):
    def stays_alive(cells, cell):
        number_of_live_neighbours = len(get_live_neighbours(cells, cell))
        return number_of_live_neighbours == 2 or number_of_live_neighbours == 3

    return [cell for cell in cells if stays_alive(cells, cell)]

def born(cells):
    def comes_alive(cells, cell):
        number_of_live_neighbours = len(get_live_neighbours(cells, cell))
        return number_of_live_neighbours == 3

    maybe_born = set(sum([ get_dead_neighbours(cells, cell)for cell in cells], []))
    return [cell for cell in maybe_born if comes_alive(cells, cell)]


def main():

    width, height = columns * cell_size, rows * cell_size
    cells = random_pattern(columns, rows)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        refresh_screen(screen, cells, cell_size, width, height)
        # clock.tick(1)
        cells = surviving(cells) + born(cells)

main()

