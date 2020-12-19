# Name:                                            Renacin Matadeen
# Date:                                               12/18/2020
# Title                                           Basics Of PyGame
#
# ----------------------------------------------------------------------------------------------------------------------
import sys
import pygame
from pygame.locals import *
import random
# ----------------------------------------------------------------------------------------------------------------------
"""
Notes:
    + Following:
        - https://www.youtube.com/watch?v=F69-t33e8tk
"""
# ----------------------------------------------------------------------------------------------------------------------


def main():

    # Window SetUp
    screen_dim = (1000, 1000)
    pygame.init()
    window = pygame.display.set_mode(screen_dim)
    pygame.display.set_caption("Simulating Particles")


    # Particle Will Be Stored In A List | Start With No Particles
    particles = []


    # Gotta Store PyGame In Main Loop | Need To Check For Events
    while True:
        window.fill((0, 0, 0))

        # Add Particles To List
        mx, my = pygame.mouse.get_pos()
        particles.append([[mx, my], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))])

        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.01
            particle[1][1] += 0.01
            pygame.draw.circle(window, particle[3], [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)

        # Check For Events | Moving Character
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()





# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
