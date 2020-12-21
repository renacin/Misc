# Name:                                            Renacin Matadeen
# Date:                                               12/18/2020
# Title                                           Functions For Pygame
#
# ----------------------------------------------------------------------------------------------------------------------
import sys
import pygame
from pygame.locals import *
from SETUP.classes import *
# ----------------------------------------------------------------------------------------------------------------------


# Initialize The Game Window
def setup_window():

    # Window SetUp & Initialize Window
    screen_dim = (1000, 1000)
    pygame.init()

    # Set Screen Size & Create Game Clock
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(screen_dim)
    pygame.display.set_caption("Falling Circles")

    return window, clock


# Initialize Some Of The Games Assets
def init_assets():
    font_path = "FONTS/IosevkaBold.ttf"
    GAME_FONT = pygame.font.Font(font_path, 60)
    hitmarker_sound = pygame.mixer.Sound("SOUNDS/HitmarkerSound.mp3")
    character_image = pygame.image.load("IMAGES/Plane.png")

    return hitmarker_sound, character_image, GAME_FONT


# Update Particles List
def update_particles(particles, window):

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

    return particles


# Print Number Of Projectiles On The Screen
def num_particles(particles, GAME_FONT, window):
    num_particle = len(particles)
    particles_text = "# Of Projectiles: [{}]".format(num_particle)
    text = GAME_FONT.render(particles_text, True, (255, 255, 255))
    window.blit(text, (40, 900))


def check_events(events, particles, hitmarker_sound):
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
