# Name:                                            Renacin Matadeen
# Date:                                               12/18/2020
# Title                                           Basics Of PyGame
#
# ----------------------------------------------------------------------------------------------------------------------
import sys

import pygame
from pygame.locals import *

import Data.config
from Data.funcs import *
# ----------------------------------------------------------------------------------------------------------------------


# Main Function Will Store Everything
def main():

    # Main Pygame Loop | Need To Check For Events
    while True:

        # Main Game Setup
        Data.config.clock.tick(Data.config.FPS)
        Data.config.window.fill((33, 33, 33))

        # Draw moving Square That Will Take Damage
        move_damage_rect(Data.config.damage_rect, Data.config.screen_dim, Data.config.window, Data.config.x_speed)

        # Update Particles List
        update_particles(Data.config.particles, Data.config.window)

        # Update Character Position On Screen
        mx, my = pygame.mouse.get_pos()
        Data.config.window.blit(Data.config.character_image, (mx-90, my-100))

        # Check For Events | Moving Character
        events_list = pygame.event.get()
        check_events(events_list, Data.config.particles, Data.config.shots_taken)

        # Check For Collision Between Damage Rectangle & Player Particles
        check_collisions(Data.config.particles, Data.config.damage_rect, Data.config.damage_done, Data.config.hitmarker_sound)

        # Print Number Of Particles In System
        game_stats(Data.config.damage_done, Data.config.shots_taken, Data.config.GAME_FONT, Data.config.window)

        # Update The Display
        pygame.display.update()


# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
