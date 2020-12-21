# Name:                                            Renacin Matadeen
# Date:                                               12/18/2020
# Title                                           Functions For Pygame
#
# ----------------------------------------------------------------------------------------------------------------------
import sys
import pygame
from pygame.locals import *
# ----------------------------------------------------------------------------------------------------------------------


# Create An Instance Of A Particle: A Particle Is:Something That Exists At A Given Time, Moves Around, Changes Over Time
def setup_window():
    # Window SetUp
    screen_dim = (1000, 1000)
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(screen_dim)
    pygame.display.set_caption("Falling Circles")

    return window, clock
