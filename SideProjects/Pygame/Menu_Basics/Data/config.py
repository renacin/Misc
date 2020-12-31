# Name:                                            Renacin Matadeen
# Date:                                               12/28/2020
# Title                            Define Global Variables That Will be Used Between Functions
#
# ----------------------------------------------------------------------------------------------------------------------
import pygame
from pygame.locals import *
# ----------------------------------------------------------------------------------------------------------------------


# FPS Clock, Basic Variables, Assests, & Particles Storage Location
game_state = True
FPS = 60

# Window SetUp & Initialize Window
background_colour = (33, 33, 33)
screen_dim = (1000, 1000)
pygame.init()

# Set Screen Size & Create Game Clock
clock = pygame.time.Clock()
window = pygame.display.set_mode(screen_dim)
pygame.display.set_caption("GUESSING GAME")

# Title Font
titlef_path = "Data/Title_BoldOblique.ttf"
title_font = pygame.font.Font(titlef_path, 60)

# user Input Font
usr_inp_font_path = "Data/Input_Thin.ttf"
usr_inp_font = pygame.font.Font(usr_inp_font_path, 30)

# Define Additional Outputs & User Inputs
user_input = "INPUT"
input_colour = (255, 255, 255)
