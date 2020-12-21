# Name:                                            Renacin Matadeen
# Date:                                               12/18/2020
# Title                                           Basics Of PyGame
#
# ----------------------------------------------------------------------------------------------------------------------
import sys
import random
import pygame
from pygame.locals import *
from SETUP.funcs import *
from SETUP.classes import *
# ----------------------------------------------------------------------------------------------------------------------


# Main Function Will Store Everything
def main():

    # Setup Window & FPS Clock
    FPS = 120
    window, clock = setup_window()
    hitmarker_sound, character_image, GAME_FONT = init_assets()

    # Particle Will Be Stored In A List | Start With No Particles
    particles = []

    # Main Pygame Loop | Need To Check For Events
    while True:

        # Main Game Setup
        clock.tick(FPS)
        window.fill((253, 92, 99))

        # Update Particles List
        particles = update_particles(particles, window)

        # Update Character Position On Screen
        mx, my = pygame.mouse.get_pos()
        window.blit(character_image, (mx-25, my-10))

        # Check For Events | Moving Character
        events_list = pygame.event.get()
        check_events(events_list, particles, hitmarker_sound)

        # Print Number Of Particles In System
        num_particles(particles, GAME_FONT, window)

        # Update The Display
        pygame.display.update()


# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
