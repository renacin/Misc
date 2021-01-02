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

main_blue = (77, 116, 185)
background_colour = (220, 221, 225)
darker_grey = (116, 120, 145)

screen_dim = (500, 500)
pygame.init()

# Set Screen Size & Create Game Clock
clock = pygame.time.Clock()
window = pygame.display.set_mode(screen_dim)
pygame.display.set_caption("Math Game")


# Title Font
titlef_path = "Data/MontserratMedium.ttf"
title_font = pygame.font.Font(titlef_path, 36)

# SubTitle Font
subtitlef_path = "Data/CardoRegular.ttf"
subtitle_font = pygame.font.Font(subtitlef_path, 16)

# user Input Font
usr_inp_font_path = "Data/Input_Thin.ttf"
usr_inp_font = pygame.font.Font(usr_inp_font_path, 30)


# Define Additional Outputs & User Inputs
input_bool = False
user_input = "INPUT"
input_colour = (255, 255, 255)
