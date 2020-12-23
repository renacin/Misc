# Name:                                            Renacin Matadeen
# Date:                                               12/18/2020
# Title                            Define Global Variables That Will be Used Between Functions
#
# ----------------------------------------------------------------------------------------------------------------------
import pygame
from pygame.locals import *

from Data.funcs import *
# ----------------------------------------------------------------------------------------------------------------------


# FPS Clock, Basic Variables, Assests, & Particles Storage Location
FPS = 120
damage_done = 0
shots_taken = 0
particles = []

# Window SetUp & Initialize Window
screen_dim = (1000, 1000)
pygame.init()

# Set Screen Size & Create Game Clock
clock = pygame.time.Clock()
window = pygame.display.set_mode(screen_dim)
pygame.display.set_caption("Simple Shooter")


# Init Font, Sound, & Sprite Assets
font_path = "Data/IosevkaBold.ttf"
GAME_FONT = pygame.font.Font(font_path, 30)
hitmarker_sound = pygame.mixer.Sound("Data/HitmarkerSound.mp3")
character_image = pygame.image.load("Data/Plane.png")

# Draw Rectangle That Will Take Damage | Only Moves Left Right
damage_rect = pygame.Rect(20, 60, 400, 25)
x_speed = 5
