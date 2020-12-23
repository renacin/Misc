# Name:                                            Renacin Matadeen
# Date:                                               12/18/2020
# Title                                           Functions For Pygame
#
# ----------------------------------------------------------------------------------------------------------------------
import sys

import pygame
from pygame.locals import *

import Data.config
from Data.classes import *
# ----------------------------------------------------------------------------------------------------------------------


# Update Particles List
def update_particles(particles, window):
    for particle in particles:

        # Process Movement Of Particle | Process X Coordinate | Y Coordinate | Larger Particle Fall Faster!!!
        particle.mouse_x = int(particle.mouse_x + particle.vel_x)                            # X Movement Left Right
        particle.mouse_y = int(particle.mouse_y + particle.vel_y)                            # Y Movement Up Down

        # Update Timer
        particle.timer = particle.timer - 0.10

        # Draw Projectile
        projectile_rect = Rect(particle.mouse_x, particle.mouse_y, particle.size[0], particle.size[1])
        pygame.draw.rect(window, particle.colour, projectile_rect)

        # Remove Particle If Time Is Up
        if particle.timer <= 0:
            Data.config.particles.remove(particle)



# Print Number Of Projectiles On The Screen
def game_stats(damage_done, shots_taken, GAME_FONT, window):

    # Print Number Of Shots Taken
    combined_text = "SHOTS {} | ".format(shots_taken)

    # Print Damage Done
    combined_text += " DMG {} | ".format(damage_done)

    # Print Overall Game Accuracy
    try:
        acc = (damage_done/shots_taken) * 100
        accuracy_ = round(acc, 0)
    except ZeroDivisionError:
        accuracy_ = 0

    accuracy_ = str(accuracy_)
    combined_text += " ACC {}%".format(accuracy_[:-2])

    # Render All To Screen
    text = GAME_FONT.render(combined_text, True, (255, 255, 255))
    window.blit(text, (280, 900))



# Check Events & Adjust Accordingly
def check_events(events, particles, shots_taken):
    for event in events:

        # Quit If Exit Button Pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Quit If Escape Button Pressed
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        # Add Particles To List If Mouse Clicked | Difference Between event.type & event.button
        if (event.type == MOUSEBUTTONUP):
            if (event.button == 1):
                mx, my = pygame.mouse.get_pos()

                # A Particle Must Take Mouse Position [X, Y], SOMETHING, SIZE, COLOUR
                new_Particle = Particle(mouse_xy=[mx, my])
                Data.config.particles.append(new_Particle)
                Data.config.shots_taken += 1



# Move Damage Rectangle
def move_damage_rect(damage_rect, screen_dimensions, window, x_speed):
    m_colour = (255, 255, 255)

    damage_rect.x += x_speed

    # Collision With Screen Borders
    if (damage_rect.right >= screen_dimensions[0]) or (damage_rect.left <= 0):
        Data.config.x_speed *= -1

    # Update Damage Rectangle
    pygame.draw.rect(window, m_colour, damage_rect)



# Check Collisons Between Particles & Damage Rectangle
def check_collisions(particles, damage_rect, damage_done, hitmarker_sound):

    col_tol = 20
    for particle in particles:

        col_part = pygame.Rect(particle.mouse_x, particle.mouse_y, particle.size[0], particle.size[1])
        if col_part.colliderect(damage_rect):

            # Top Collision
            if abs(col_part.top - damage_rect.bottom) <= col_tol:

                # Play Hitmarker Sound For Every Projectile Fired
                pygame.mixer.Sound.play(hitmarker_sound)
                pygame.mixer.music.stop()

                # Remove The Particle
                Data.config.particles.remove(particle)
                Data.config.damage_done += 1
