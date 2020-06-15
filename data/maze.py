"""
This module contains Maze and Cell classes that used for maze generation.
"""
from random import randint

import pygame as pg

from .globals import CELL_SIZE, WHITE, SCREEN_HEIGHT, SCREEN_WIDTH, ORANGE


class Cell(object):
    """ Cells class creates and draw walls of cell.
    """
    def __init__(self, col, row):
        self._col = col
        self._row = row
        self._x = col * CELL_SIZE
        self._y = row * CELL_SIZE
        self._visited = False
        self._walls = {
            'top': True,
            'right': True,
            'bottom': True,
            'left': True,
        }
        self._neighbours = []

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, flag):
        self._visited = flag

    @property
    def neighbours(self):
        return self._neighbours

    @property
    def col(self):
        return self._col

    @property
    def row(self):
        return self._row

    def _check_neighbours(self):
        if self._neighbours:
            self._neighbours = [neighbour for neighbour in self._neighbours if not neighbour.visited]

    def get_neighbour(self):
        self._check_neighbours()
        if not self._neighbours:
            return None
        return self._neighbours[randint(0, len(self._neighbours) - 1)]

    def draw(self, screen):
        """ Draw walls of cell if they exists. """
        if self._visited:
            pg.draw.rect(screen, ORANGE, (self._x, self._y, CELL_SIZE, CELL_SIZE))

        if self._walls['top']:
            pg.draw.line(screen, WHITE, (self._x, self._y), (self._x + CELL_SIZE, self._y), 1)
        if self._walls['right']:
            pg.draw.line(screen, WHITE, (self._x + CELL_SIZE, self._y), (self._x + CELL_SIZE, self._y + CELL_SIZE), 1)
        if self._walls['bottom']:
            pg.draw.line(screen, WHITE, (self._x + CELL_SIZE, self._y + CELL_SIZE), (self._x, self._y + CELL_SIZE), 1)
        if self._walls['left']:
            pg.draw.line(screen, WHITE, (self._x, self._y + CELL_SIZE), (self._x, self._y), 1)


class Maze(object):
    """ Maze class creates and draws grid of cells.
    """
    def __init__(self):
        self._grid = []
        self._cols = SCREEN_WIDTH // CELL_SIZE
        self._rows = SCREEN_HEIGHT // CELL_SIZE
        self._build_grid()
        self._current_cell = self._grid[0]

    def _build_grid(self):
        """ Build grid of cells. """
        for row in range(self._rows):
            for col in range(self._cols):
                cell = Cell(col, row)
                self._grid.append(cell)

        for cell in self._grid:
            top = self._cell_neighbour_index(cell.col, cell.row - 1)
            right = self._cell_neighbour_index(cell.col + 1, cell.row)
            bottom = self._cell_neighbour_index(cell.col, cell.row + 1)
            left = self._cell_neighbour_index(cell.col - 1, cell.row)

            for index in [top, right, bottom, left]:
                if index is not None:
                    cell.neighbours.append(self._grid[index])

    def _cell_neighbour_index(self, col, row):
        if col < 0 or row < 0 or col > self._cols - 1 or row > self._rows - 1:
            return
        return col + row * self._cols

    def _update(self):
        self._current_cell.visited = True
        next_cell = self._current_cell.get_neighbour()
        if next_cell:
            self._current_cell = next_cell

    def draw(self, screen):
        """ Draw all cells on the screen. """
        self._update()

        for cell in self._grid:
            cell.draw(screen)
