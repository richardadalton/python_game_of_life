import sys
import argparse
import pygame
from patterns import random_pattern, glider_pattern
from screen import refresh_screen

#Options
DEFAULT_COLS, DEFAULT_ROWS = 100, 50
DEFAULT_CELL_SIZE = 10
DEFAULT_AGING = 0

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--cell_size", type=int, default=DEFAULT_CELL_SIZE,
                        help="The size of a cell within the grid")
    parser.add_argument("-r", "--rows", type=int, default=DEFAULT_ROWS,
                        help="The number of rows in the grid")
    parser.add_argument("-c", "--columns", type=int, default=DEFAULT_COLS,
                        help="The number of columns in the grid")
    parser.add_argument("-a", "--aging", type=int, default=DEFAULT_AGING,
                        help="The number of generations that a living cell survives.  Default is forever.")

    return parser.parse_args()


def wrap_neighbour(neighbour):
    (c, r) = neighbour
    c = 0 if c == args.columns else c
    c = args.columns - 1 if c == -1 else c
    r = 0 if r == args.rows else r
    r = args.rows - 1 if r == -1 else r
    return (c, r)


def wrap_neighbours(neighbours):
    return [ wrap_neighbour(n) for n in neighbours]


# Finding Neighbours
def get_neighbours(cell):
    (c, r) = cell
    neighbours =  [(c - 1, r - 1), (c, r - 1), (c + 1, r - 1),
                   (c + 1, r),                 (c + 1, r + 1),
                   (c, r + 1), (c - 1, r + 1), (c - 1, r)]
    return wrap_neighbours(neighbours)

def get_live_neighbours(cells, cell):
    (c, r) = cell
    neighbours = get_neighbours((c, r))
    return [val for val in neighbours if val in cells]

def get_dead_neighbours(cells, cell):
    (c, r) = cell
    neighbours = get_neighbours(cell)
    return [val for val in neighbours if val not in cells]


# Living And Dying
def surviving(cells):
    def stays_alive(cells, cell):
        number_of_live_neighbours = len(get_live_neighbours(cells, cell))
        return number_of_live_neighbours == 2 or number_of_live_neighbours == 3

    if args.aging == DEFAULT_AGING:
        return {cell: cells[cell] for cell in cells if stays_alive(cells, cell)}
    else:
        return {cell: cells[cell] + 1 for cell in cells if stays_alive(cells, cell)}

def born(cells):
    def comes_alive(cells, cell):
        number_of_live_neighbours = len(get_live_neighbours(cells, cell))
        return number_of_live_neighbours == 3

    maybe_born = set(sum([ get_dead_neighbours(cells, cell)for cell in cells], []))
    return {cell: 0 for cell in maybe_born if comes_alive(cells, cell)}

def next_generation(cells):
    next_gen = {}
    next_gen.update(surviving(cells))
    next_gen.update(born(cells))
    return next_gen

def main():
    width, height = args.columns * args.cell_size, args.rows * args.cell_size
    cells = random_pattern(args.columns, args.rows)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        refresh_screen(screen, cells, args.cell_size, width, height)
        clock.tick(1)
        cells = next_generation(cells)

if __name__ == '__main__':
    args = get_arguments()
    main()

