"""
This module contains main Game class
"""

import pygame as pg

from .globals import SCREEN_SIZE


class Game(object):
    """ Game class for entire project.
    """
    def __init__(self, caption):
        self._caption = caption
        self._screen = pg.display.set_mode(SCREEN_SIZE)
        self._stop = False

    def event_loop(self):
        """ Process all events. """
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self._stop = True

            if event.type == pg.QUIT:
                self._stop = True

    def update(self):
        """ Update the display. """
        pg.display.update()

    def main_loop(self):
        """ Main loop for entire project. """
        while not self._stop:
            self.event_loop()
            self.update()
