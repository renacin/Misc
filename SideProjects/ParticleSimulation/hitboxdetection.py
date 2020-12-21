# Name:                                            Renacin Matadeen
# Date:                                               12/18/2020
# Title                                    Basics Of PyGame: Hitbox Detection
#
# ----------------------------------------------------------------------------------------------------------------------
import sys
import random
import pygame
from pygame.locals import *
# ----------------------------------------------------------------------------------------------------------------------


# Moving Rectangles
def move_rectangles(screen, rect, x_speed, y_speed, screen_dimensions, colour, list_of_hitboxes):

    rect.x += x_speed
    rect.y += y_speed

    # Collision With Screen Borders
    if (rect.right >= screen_dimensions[0]) or (rect.left <= 0):
        x_speed *= -1

    if (rect.bottom >= screen_dimensions[1]) or (rect.top <= 0):
        y_speed *= -1


    # Check Collisions With Other Shapes
    col_tol = 15
    for shape_ in list_of_hitboxes:
        if rect != shape_:
            if rect.colliderect(shape_):

                # Top Collision
                if abs(rect.top - shape_.bottom) < col_tol:
                    y_speed *= -1

                # Bottom Collision
                if abs(rect.bottom - shape_.top) < col_tol:
                    y_speed *= -1

                # Left Collision
                if abs(rect.left - shape_.right) < col_tol:
                    x_speed *= -1

                # Right Collision
                if abs(rect.right - shape_.left) < col_tol:
                    x_speed *= -1


    pygame.draw.rect(screen, colour, rect)

    return x_speed, y_speed





# Main Function Will Store Everything
def main():

    # Setup Window & FPS Clock
    FPS = 60
    pygame.init()
    clock = pygame.time.Clock()
    screen_dimensions = (1000, 1000)
    screen_colour = (30, 30, 30)
    screen = pygame.display.set_mode(screen_dimensions)

    # Create Moving Rectangle
    moving_rect = pygame.Rect(350, 350, 100, 100)
    m_colour = (255, 255, 255)
    x_speed, y_speed = 5, 4

    # Create Stationary Rectangle
    stationary_rect = Rect(300, 600, 200, 200)
    s_colour = (255, 0, 0)
    oth_x_speed, oth_y_speed = 5, 4

    list_of_hitboxes = [moving_rect, stationary_rect]

    # Main Pygame Loop | Need To Check For Events
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(screen_colour)

        x_speed, y_speed = move_rectangles(screen, moving_rect, x_speed, y_speed, screen_dimensions, m_colour, list_of_hitboxes)
        oth_x_speed, oth_y_speed = move_rectangles(screen, stationary_rect, oth_x_speed, oth_y_speed, screen_dimensions, s_colour, list_of_hitboxes)

        pygame.display.flip()
        clock.tick(FPS)

# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
