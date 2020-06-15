"""
This module contains the start function.
It initiates pygame, creates an instance of data.main.Game class and activates the main loop of project.
"""

import pygame as pg

from data import main


def start():
    pg.init()

    game = main.Game('Maze')
    game.main_loop()

    pg.quit()


if __name__ == '__main__':
    start()
