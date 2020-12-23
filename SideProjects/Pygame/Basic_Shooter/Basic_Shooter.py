# Name:                                            Renacin Matadeen
# Date:                                               12/18/2020
# Title                                           Basics Of PyGame
#
# ----------------------------------------------------------------------------------------------------------------------
import sys
import random
import pygame
from pygame.locals import *
from Data.funcs import *
from Data.classes import *
# ----------------------------------------------------------------------------------------------------------------------


# Main Function Will Store Everything
def main():

    # Setup Window & FPS Clock
    FPS = 120
    window, clock, screen_dim = setup_window()
    hitmarker_sound, character_image, GAME_FONT, damage_rect, x_speed = init_assets()
    damage_done = 0
    shots_taken = 0

    # Particle Will Be Stored In A List | Start With No Particles
    particles = []

    # Main Pygame Loop | Need To Check For Events
    while True:

        # Main Game Setup
        clock.tick(FPS)
        window.fill((33, 33, 33))

        # Draw moving Square That Will Take Damage
        x_speed = move_damage_rect(damage_rect, screen_dim, window, x_speed)

        # Update Particles List
        particles = update_particles(particles, window)

        # Update Character Position On Screen
        mx, my = pygame.mouse.get_pos()
        window.blit(character_image, (mx-90, my-100))

        # Check For Events | Moving Character
        events_list = pygame.event.get()
        shots_taken = check_events(events_list, particles, shots_taken)

        # Check For Collision Between Damage Rectangle & Player Particles
        particles, damage_done = check_collisions(particles, damage_rect, damage_done, hitmarker_sound)

        # Print Number Of Particles In System
        game_stats(damage_done, shots_taken, GAME_FONT, window)

        # Update The Display
        pygame.display.update()


# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
