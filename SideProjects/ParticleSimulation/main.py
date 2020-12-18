# Name:                                            Renacin Matadeen
# Date:                                               12/18/2020
# Title                                           Basics Of PyGame
#
# ----------------------------------------------------------------------------------------------------------------------
import time
import pygame
import random
import math
# ----------------------------------------------------------------------------------------------------------------------
"""
Notes:
    + Following:
        - https://www.youtube.com/watch?v=i6xMBig-pP4
"""
# ----------------------------------------------------------------------------------------------------------------------
def main():

    # Basic SetUp
    screen_width = 1000
    screen_height = 1000

    pygame.init()   # Initialize Pygame
    window = pygame.display.set_mode((screen_height, screen_width))    # Set Window Size
    pygame.display.set_caption("First Game")    # Set Name Of Game

    # SetUp Character
    x = 0
    y = 0
    width = 20
    height = 20

    # Set The Speed At Which The Character Moves
    vel = 5

    # Start Colour
    char_colour = (0, 0, 0)

    # Gotta Store PyGame In Main Loop | Need To Check For Events
    window.fill((255, 255, 255))
    execute_app = True
    while execute_app:
        pygame.time.delay(10)  #Delay Each Iteration By 100 Milliseconds

        # Check For Events | Moving Character
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                execute_app = False


        # Draw Stuff | Need To Refresh | Need To Create New Screen As To Not Drag Character
        #window.fill((255, 255, 255))
        pygame.draw.rect(window, char_colour, (x, y, width, height))    # Surface, Colour(255, 255, 255), Rect(X, Y, Width, Height)


        # Update Arrow Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
        if keys[pygame.K_RIGHT] and x < screen_width - width - vel:
            x += vel
        if keys[pygame.K_UP] and y > vel:
            y -= vel * 0.5
        if keys[pygame.K_DOWN] and y < screen_height - height - vel:
            y += vel

        # Character Behaviour
        if keys[pygame.K_SPACE]:
            char_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            width = random.randint(10, 40)
            height = width
            pygame.time.delay(100)  #Delay Each Iteration By 100 Milliseconds

        pygame.display.update()



    # Quit The Game
    pygame.quit()



# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
