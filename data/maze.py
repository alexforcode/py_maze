"""
This module contains Maze and Cell classes that used for maze generation.
"""
import pygame as pg

from .globals import CELL_SIZE, WHITE, SCREEN_HEIGHT, SCREEN_WIDTH


class Maze(object):
    """ Maze class creates and draws grid of cells.
    """
    def __init__(self):
        self._grid = []
        self._cols = SCREEN_WIDTH // CELL_SIZE
        self._rows = SCREEN_HEIGHT // CELL_SIZE
        self._build_grid()

    def _build_grid(self):
        """ Build grid of cells. """
        for col in range(self._cols):
            for row in range(self._rows):
                cell = Cell(col, row)
                self._grid.append(cell)

    def draw(self, screen):
        """ Draw all cells on the screen. """
        for cell in self._grid:
            cell.draw(screen)


class Cell(object):
    """ Cells class creates and draw walls of cell.
    """
    def __init__(self, col, row):
        self._x = col * CELL_SIZE
        self._y = row * CELL_SIZE
        self._walls = {
            'top': True,
            'right': True,
            'bottom': True,
            'left': True,
        }

    def draw(self, screen):
        """ Draw walls of cell if they exists. """
        if self._walls['top']:
            pg.draw.line(screen, WHITE, (self._x, self._y), (self._x + CELL_SIZE, self._y), 1)
        if self._walls['right']:
            pg.draw.line(screen, WHITE, (self._x + CELL_SIZE, self._y), (self._x + CELL_SIZE, self._y + CELL_SIZE), 1)
        if self._walls['bottom']:
            pg.draw.line(screen, WHITE, (self._x + CELL_SIZE, self._y + CELL_SIZE), (self._x, self._y + CELL_SIZE), 1)
        if self._walls['left']:
            pg.draw.line(screen, WHITE, (self._x, self._y + CELL_SIZE), (self._x, self._y), 1)
