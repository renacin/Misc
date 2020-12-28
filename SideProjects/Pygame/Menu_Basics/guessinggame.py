# Name:                                            Renacin Matadeen
# Date:                                               12/27/2020
# Title                                     Basics Of PyGame Menus & Buttons
#
# ----------------------------------------------------------------------------------------------------------------------
import pygame
from pygame.locals import *

import Data.config as lnk
from Data.funcs import *
# ----------------------------------------------------------------------------------------------------

# Main Function Will Store Everything
def main():

    while lnk.game_state:

        # Fill Background Window
        lnk.window.fill(lnk.background_colour)

        # Draw Title Screen
        draw_title_card()

        # Check For Events In Game
        events_list = pygame.event.get()
        check_events(events_list)

        # Update The Screen
        pygame.display.update()

    pygame.quit()

# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
