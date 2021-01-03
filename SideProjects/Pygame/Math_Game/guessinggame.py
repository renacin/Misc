# Name:                                            Renacin Matadeen
# Date:                                               12/27/2020
# Title                                     Basics Of PyGame Menus & Buttons
#
# ----------------------------------------------------------------------------------------------------------------------
import pygame
from pygame.locals import *

import Data.config as lnk
from Data.funcs import *
from Data.ui import *
# ----------------------------------------------------------------------------------------------------

# Main Function Will Store Everything
def main():

    while lnk.game_state:

        # Draw User Interface
        draw_ui()

        # Check For Events In Game
        check_events(pygame.event.get())

        # Update The Entire Screen
        pygame.display.flip()

    # If Game State Changes To False; Break Loop And End Game
    pygame.quit()

# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
