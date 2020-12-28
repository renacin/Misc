# Name:                                            Renacin Matadeen
# Date:                                               12/27/2020
# Title                                     Basics Of PyGame Menus & Buttons
#
# ----------------------------------------------------------------------------------------------------------------------
import pygame
from pygame.locals import *

import Data.config
from Data.classes import *
# ----------------------------------------------------------------------------------------------------

# Main Function Will Store Everything
def main():

    #define colours
    bg = (33, 33, 33)
    black = (0, 0, 0)

    again = Button(400, 200, 'Again?')
    quit = Button(600, 200, 'Quit?')
    down = Button(400, 350, 'Down')
    up = Button(600, 350, 'Up')


    run = True
    while run:
        Data.config.screen.fill(bg)

        if again.draw_button():
            print('Again')
            Data.config.counter = 0

        if quit.draw_button():
            print('Quit')

        if up.draw_button():
            print('Up')
            Data.config.counter += 1

        if down.draw_button():
            print('Down')
            Data.config.counter -= 1

        counter_img = Data.config.font.render(str(Data.config.counter), True, black)
        Data.config.screen.blit(counter_img, (600, 450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
