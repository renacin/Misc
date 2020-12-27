# Name:                                            Renacin Matadeen
# Date:                                               12/27/2020
# Title                            Define Global Variables That Will be Used Between Functions
#
# ----------------------------------------------------------------------------------------------------------------------
import pygame
from pygame.locals import *
# ----------------------------------------------------------------------------------------------------------------------


# FPS Clock, Basic Variables, Assests, & Particles Storage Location
FPS = 120

# Window SetUp & Initialize Window
screen_dim = (1000, 1000)
pygame.init()

# Set Screen Size & Create Game Clock
clock = pygame.time.Clock()
screen = pygame.display.set_mode(screen_dim)
pygame.display.set_caption("Understanding Buttons")


# Init Font, Sound, & Sprite Assets
font_path = "Data/IosevkaBold.ttf"
font = pygame.font.Font(font_path, 30)


#define global variable
clicked = False
counter = 0
