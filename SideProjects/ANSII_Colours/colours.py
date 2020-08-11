# Name:                                            Renacin Matadeen
# Date:                                               08/09/2020
# Title                                 Implementing ASCII Colours Wihtin Terminal
#
# ----------------------------------------------------------------------------------------------------------------------
import time
# ----------------------------------------------------------------------------------------------------------------------
"""
References:
    +

Notes:
    + How can I use colours as a terminal output within my programs?
        - ANSI escape sequences style outputs in certain ways
        - They follow the general pattern
            "\033[m"

        - Use semi colons to stack parameters!
            "\033[32;42;1m"

    +       TEXT ATTRIBUTES
            1	Bold on
            4	Underscore (on monochrome display adapter only)
            7	Reverse video on
            8	Concealed on

    +       FONT COLOUR
            30	Black
            31	Red
            32	Green
            33	Yellow
            34	Blue
            35	Magenta
            36	Cyan
            37	White

    +       BACKGROUND COLOUR
            40	Black
            41	Red
            42	Green
            43	Yellow
            44	Blue
            45	Magenta
            46	Cyan
            47	White

"""
# ----------------------------------------------------------------------------------------------------------------------

class ANSI_CODE:

    # These ANSI codes change the character colour
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    TEST = '\033[1;37;41m'

    # These ANSI codes change the character type
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    # Follow All Instructions With ANSI Reset Code!
    RESET = '\033[0m'

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print(ANSI_CODE.TEST + " 0_0 " + ANSI_CODE.RESET)
