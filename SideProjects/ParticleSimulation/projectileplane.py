# Name:                                            Renacin Matadeen
# Date:                                               12/18/2020
# Title                                           Basics Of PyGame
#
# ----------------------------------------------------------------------------------------------------------------------
import sys
import random
import pygame
from pygame.locals import *
from SETUP.funcs import *

# ----------------------------------------------------------------------------------------------------------------------
"""
Notes:
    + Following:
        - https://www.youtube.com/watch?v=F69-t33e8tk
"""
# ----------------------------------------------------------------------------------------------------------------------


# Create An Instance Of A Particle: A Particle Is:Something That Exists At A Given Time, Moves Around, Changes Over Time
class Particle:

    # Characteristics Of Particle That Are Needed
    def __init__(self, mouse_xy=[0, 0], velocityxy=[0, -10], radius=5, timer=10, colour=(255, 255, 255)):

        # Spawn Particle At Mouse Coordinates
        self.mouse_x = int(mouse_xy[0])
        self.mouse_y = int(mouse_xy[1])

        # Give Particle Velocity On Both XY Axis | X = Left Right | Y Means Up Or Down
        self.vel_x = int(velocityxy[0])
        self.vel_y = int(velocityxy[1])

        # Define Radius Of Particle
        self.radius = radius

        # How Long Will The Particle Last | Even Out Of Frame
        self.timer = timer

        # Define The Particle's Colour
        self.colour = colour



def main():

    # Setup Window & FPS Clock
    FPS = 120
    window, clock = setup_window()

    # Needed Assests To Import
    font_path = "FONTS/IosevkaBold.ttf"
    GAME_FONT = pygame.font.Font(font_path, 60)
    hitmarker_sound = pygame.mixer.Sound("SOUNDS/HitmarkerSound.mp3")
    character_image = pygame.image.load("IMAGES/Plane.png")


    # Particle Will Be Stored In A List | Start With No Particles
    particles = []


    # SetUp Character



    # Gotta Store PyGame In Main Loop | Need To Check For Events
    while True:
        clock.tick(FPS)
        window.fill((253, 92, 99))



        # Process Each Particle In Particles List
        for particle in particles:

            # Process Movement Of Particle | Process X Coordinate | Y Coordinate | Larger Particle Fall Faster!!!
            particle.mouse_x = int(particle.mouse_x + particle.vel_x)                            # X Movement Left Right
            particle.mouse_y = int(particle.mouse_y + particle.vel_y)                            # Y Movement Up Down

            # Update Timer
            particle.timer = particle.timer - 0.05

            # Draw Circle
            pygame.draw.circle(window, particle.colour, [particle.mouse_x, particle.mouse_y], particle.radius)

            # Remove Particle If Time Is Up
            if particle.timer <= 0:
                particles.remove(particle)




        # Update Character Movement
        mx, my = pygame.mouse.get_pos()
        window.blit(character_image, (mx-25, my-10))




        # Check For Events | Moving Character
        for event in pygame.event.get():

            # Quit If Exit Button Pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Quit If Escape Button Pressed
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # Add Particles To List If Mouse Clicked
            if (event.type == MOUSEWHEEL) or (event.type == MOUSEBUTTONDOWN):
                if len(particles) < 1000:
                    mx, my = pygame.mouse.get_pos()

                    # A Particle Must Take Mouse Position [X, Y], SOMETHING, SIZE, COLOUR
                    new_Particle = Particle(mouse_xy=[mx, my], radius=5)
                    particles.append(new_Particle)

                    # Play Hitmarker Sound For Every Projectile Fired
                    pygame.mixer.Sound.play(hitmarker_sound)
                    pygame.mixer.music.stop()



        # Print Number Of Particle In System
        num_particle = len(particles)
        particles_text = "# Of Projectiles: [{}]".format(num_particle)
        text = GAME_FONT.render(particles_text, True, (255, 255, 255))
        window.blit(text, (40, 900))





        pygame.display.update()





# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
