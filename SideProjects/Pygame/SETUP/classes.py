# Name:                                            Renacin Matadeen
# Date:                                               12/18/2020
# Title                                           Classes For Pygame
#
# ----------------------------------------------------------------------------------------------------------------------
import sys
import pygame
from pygame.locals import *
# ----------------------------------------------------------------------------------------------------------------------


# Create An Instance Of A Particle: A Particle Is:Something That Exists At A Given Time, Moves Around, Changes Over Time
class Particle:

    # Characteristics Of Particle That Are Needed
    def __init__(self, mouse_xy=[0, 0], velocityxy=[0, -10], size=(10,10), timer=10, colour=(255, 255, 255)):

        # Spawn Particle At Mouse Coordinates
        self.mouse_x = int(mouse_xy[0])
        self.mouse_y = int(mouse_xy[1])

        # Give Particle Velocity On Both XY Axis | X = Left Right | Y Means Up Or Down
        self.vel_x = int(velocityxy[0])
        self.vel_y = int(velocityxy[1])

        # Define Radius Of Particle
        self.size = size

        # How Long Will The Particle Last | Even Out Of Frame
        self.timer = timer

        # Define The Particle's Colour
        self.colour = colour
