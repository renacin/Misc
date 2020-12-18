# Name:                                            Renacin Matadeen
# Date:                                               12/15/2020
# Title                                          Particle Simulation
#
# ----------------------------------------------------------------------------------------------------------------------
import time
import pygame
import math
# ----------------------------------------------------------------------------------------------------------------------
"""
Notes:
    + Following:
        - https://www.youtube.com/watch?v=Wyv5TnkFuxE
        - https://www.youtube.com/channel/UCN7uBodTAg8KcsuDiJ9u4Rg

"""
# ----------------------------------------------------------------------------------------------------------------------
def main():

    # Basic SetUp
    pygame.init()   # Initialize Pygame
    window = pygame.display.set_mode((1000, 1000))    # Set Window Size
    pygame.display.set_caption("First Game")    # Set Name Of Game

    # SetUp Character
    x = 50
    y = 50
    width = 20
    height = 20

    # Set The Speed At Which The Character Moves
    vel = 10

    # Gotta Store PyGame In Main Loop | Need To Check For Events
    run = True
    while run:
        pygame.time.delay(10)  #Delay Each Iteration By 100 Milliseconds

        # Check For Events | Moving Character
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update Arrow Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= vel
        if keys[pygame.K_RIGHT]:
            x += vel
        if keys[pygame.K_UP]:
            y -= vel
        if keys[pygame.K_DOWN]:
            y += vel


        # Draw Stuff | Need To Refresh | Need To Create New Screen As To Not Drag Character
        window.fill((255, 255, 255))
        pygame.draw.rect(window, (0, 0, 0), (x, y, width, height))    # Surface, Colour(255, 255, 255), Rect(X, Y, Width, Height)
        pygame.display.update()



    # Quit The Game
    pygame.quit()



# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
