# Name:                                            Renacin Matadeen
# Date:                                               12/28/2020
# Title                            Define Global Variables That Will be Used Between Functions
#
# ----------------------------------------------------------------------------------------------------------------------
import pygame
from pygame.locals import *
from datetime import date
# ----------------------------------------------------------------------------------------------------------------------

# FPS Clock, Basic Variables, Assests
today = date.today()
cur_date = today.strftime("%d/%m/%Y")
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

# ----------------------------------------------------------------------------------------------------------------------

# Title Font & Rect
title_rect = pygame.Rect(34, 34, 170, 47)
titlef_path = "Data/Fonts/MontserratMedium.ttf"
title_font = pygame.font.Font(titlef_path, 36)

# SubTitle Font
subtitlef_path = "Data/Fonts/CardoRegular.ttf"
subtitle_font = pygame.font.Font(subtitlef_path, 16)

# User Input Font
usr_inp_font = pygame.font.Font(titlef_path, 15)

# ----------------------------------------------------------------------------------------------------------------------

# Draw Boxes That Will Segment User Interface


# ----------------------------------------------------------------------------------------------------------------------

# Define Additional Outputs & User Inputs

input_bool = False
user_input = "INPUT"
input_colour = (255, 255, 255)
