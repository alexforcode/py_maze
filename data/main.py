"""
This module contains main Game class.
"""

import pygame as pg

from .maze import Maze
from .globals import SCREEN_HEIGHT, SCREEN_WIDTH, DEFAULT_CAPTION, GREY, FPS


class Game(object):
    """ Game class for entire project.
    """
    def __init__(self, caption=None):
        self._caption = caption or DEFAULT_CAPTION
        pg.display.set_caption(self._caption)
        self._maze = Maze()
        self._screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._clock = pg.time.Clock()
        self._stop = False

    def _event_loop(self):
        """ Process all events. """
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self._stop = True

            if event.type == pg.QUIT:
                self._stop = True

    def _draw(self):
        """ Draw objects on screen. """
        self._maze.draw(self._screen)

    def main_loop(self):
        """ Main loop for entire project. """
        while not self._stop:
            self._clock.tick(FPS)
            self._screen.fill(GREY)
            self._event_loop()
            self._draw()
            pg.display.update()
