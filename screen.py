import pygame
from colours import dark_blue, green, black

def clear_screen(screen):
    screen.fill((0, 0, 0))

def draw_grid(screen, width, height, cell_size):
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, dark_blue, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, dark_blue, (0, y), (width, y))

def draw_cells(screen, cell_size, cells):
    for (x, y) in cells:
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, green, rectangle)

def refresh_screen(screen, cells, cell_size, width, height):
    clear_screen(screen)
    draw_cells(screen, cell_size, cells)
    draw_grid(screen, width, height, cell_size)
    pygame.display.update()
