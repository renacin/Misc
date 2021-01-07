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
num_of_questions = 2
warning_timer = 600
today = date.today()
cur_date = today.strftime("%d/%m/%Y")
game_state = True
FPS = 60

main_blue = (77, 116, 185)
background_colour = (220, 221, 225)
darker_grey = (116, 120, 145)
submit_font_colour = darker_grey

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

# Button Fonts
button_font = pygame.font.Font(titlef_path, 15)

# ----------------------------------------------------------------------------------------------------------------------

# Define Additional Outputs & User Inputs

terms = ["1", "2", "3", "4"]
question_state = False
input_message_state = False
input_message_timer = warning_timer

usr_score = 0
usr_answer = "???"
input_bool = False
usr_answer_colour = darker_grey

question_num = 1
answer_state = "N/A"

submit_button_clicked = False
submit_button_hover = False
click_timer = 0
answer_timer = 0
