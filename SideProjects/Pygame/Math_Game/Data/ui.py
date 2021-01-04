# Name:                                            Renacin Matadeen
# Date:                                               12/28/2020
# Title                                          UI Elements For Pygame
#
# ----------------------------------------------------------------------------------------------------------------------
import sys

import pygame
from pygame.locals import *

import Data.config as lnk
from Data.funcs import *
# ----------------------------------------------------------------------------------------------------------------------


# Create A Class To Help UI Development For Elements With Borders
class bordered_rect:

    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render_shape(self):

        border_px = 3

        # Draw Blue Rect Bottom
        blue_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(lnk.window, lnk.main_blue, blue_rect)

        # Draw Grey Rect Top
        grey_rect = pygame.Rect((self.x + border_px),
                                (self.y + border_px),
                                (self.width - (border_px * 2)),
                                (self.height - (border_px * 2)))

        pygame.draw.rect(lnk.window, lnk.background_colour, grey_rect)


# ----------------------------------------------------------------------------------------------------------------------


# Draw The Box That Will Store The User's Input
def draw_boxes():

    # Draw Box That Will Show Question
    bordered_rect(109, 200, 280, 100).render_shape()

    # Draw Box That Will Cover Stroke On Top Box; For Style
    masking_rect = pygame.Rect(163, 185, 173, 25)
    pygame.draw.rect(lnk.window, lnk.background_colour, masking_rect)

    # Draw Box That Will Store Answer
    bordered_rect(109, 350, 111, 40).render_shape()

    # Draw Box That Will Store Button
    bordered_rect(279, 350, 111, 40).render_shape()


# Draw Title Screen
def draw_text():

    # Draw Backing Rectangle For Title | Remember [X, Y, Width, Height]
    pygame.draw.rect(lnk.window, lnk.main_blue, lnk.title_rect)

    # Draw Title Ontop Of Rectangle For Title | Remember [X, Y] Y May Vary Due To Height
    title_text = "Math 101"
    title_render = lnk.title_font.render(title_text, True, lnk.background_colour)
    lnk.window.blit(title_render, (40, 35))

    # Draw SubTitle 1 Below Title
    subtitle_text_1 = "A simple test of your math skills"
    subtitle_text_1_render = lnk.subtitle_font.render(subtitle_text_1, True, lnk.darker_grey)
    lnk.window.blit(subtitle_text_1_render, (36, 105))

    # Draw SubTitle 2 Below Title
    subtitle_text_1 = "Tests are randomly generated"
    subtitle_text_1_render = lnk.subtitle_font.render(subtitle_text_1, True, lnk.darker_grey)
    lnk.window.blit(subtitle_text_1_render, (36, 125))



    # Draw Current Date
    curdate_render = lnk.usr_inp_font.render(lnk.cur_date, True, lnk.darker_grey)
    lnk.window.blit(curdate_render, (390, 35))



    # Draw Current Question Number
    question_title = "Question {}.".format(lnk.question_num)
    question_title_render = lnk.subtitle_font.render(question_title, True, lnk.darker_grey)
    lnk.window.blit(question_title_render, (210, 190))



    # Draw Answer Question Area With The Users Answer
    answer_area = "X = {}".format(lnk.usr_answer)
    answer_area_render = lnk.button_font.render(answer_area, True, lnk.usr_answer_colour)
    lnk.window.blit(answer_area_render, (141, 360))

    # Draw Submit Buttom
    submit_text = "SUBMIT"
    submit_text_render = lnk.button_font.render(submit_text, True, lnk.darker_grey)
    lnk.window.blit(submit_text_render, (307, 360))



    # Draw Any Warning Messages
    if lnk.input_message_state == True:
        if lnk.input_message_timer >= 0:
            warning_message = "*Invalid Entry"
            warning_message_render = lnk.subtitle_font.render(warning_message, True, lnk.darker_grey)
            lnk.window.blit(warning_message_render, (105, 325))
            lnk.input_message_timer -= 1

        else:
            lnk.input_message_state = False
            lnk.input_message_timer = lnk.warning_timer




    # Draw If Answer Was Correct Or Not
    answer_status = "Answer: {}".format(lnk.answer_state)
    answer_status_render = lnk.button_font.render(answer_status, True, lnk.main_blue)
    lnk.window.blit(answer_status_render, (185, 416))

    # Draw Current Score
    cur_score = "Score: {} / {}".format(lnk.usr_score, lnk.question_num)
    cur_score_render = lnk.button_font.render(cur_score, True, lnk.main_blue)
    lnk.window.blit(cur_score_render, (210, 436))

    # Render Current Question Only If Question State Is False | Update Status Once Complete
    if lnk.question_state == False:

        # Load Question
        terms = create_question()
        lnk.terms = terms

        # Render Question
        question_text = "{} {} {} = X".format(terms[0], terms[1], terms[2])
        question_text_render = lnk.title_font.render(question_text, True, lnk.darker_grey)
        lnk.window.blit(question_text_render, (163, 230))
        lnk.question_state = True

    else:

        # Render Question
        question_text = "{} {} {} = X".format(lnk.terms[0], lnk.terms[1], lnk.terms[2])
        question_text_render = lnk.title_font.render(question_text, True, lnk.darker_grey)
        lnk.window.blit(question_text_render, (163, 230))


# ----------------------------------------------------------------------------------------------------------------------


# Draw Entire UI Contains Other Elements
def draw_ui():

    # Fill Background Window
    lnk.window.fill(lnk.background_colour)

    # Draw Input Box
    draw_boxes()

    # Draw Title Screen
    draw_text()
