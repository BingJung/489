# modified from the pygame file provided on Canvas

# (1) import useful modules
import pygame, os, sys, random, time
from pygame.locals import *

# (2) Seed random number generator
random.seed(os.urandom(99))  # <-- unnecessary superstitious behaviour

# (3) Define screen parameters as global constants
screen_width  = 1920 # 1024
screen_height = 1080 # 768
text_height   = 36

vert_midline = int(round(screen_width/2)) # the vertical midline
horiz_midline = int(round(screen_height/2))

# (4) Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHTGRAY = (250,250,250) # <-- will be the default background color
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,50)
ORANGE = (255,100,0)
BROWN = (155, 30, 0)
BLUE = (50,150,255)
LIGHTBLUE = (100, 175, 255)
GRAY = (150,150,150)
DARKGRAY = (50, 50, 50)
DARKBLUE = (0,0,150) #(0, 0, 255)

# (5) init Pygame and font; define screen
pygame.init()
display_flags = HWSURFACE
screen = pygame.display.set_mode((screen_width, screen_height), display_flags)
font = pygame.font.SysFont('times', text_height)
pygame.mouse.set_visible(True)
pygame.font.init()


# (6) define some useful functions that will almost certainly get used
def blit_text(message, line):
    # formats, renders and blits a message to screen on the designated line
    #   but does NOT update the screen.
    # it is for use in cases where it is necessary to put several lines of
    #   text on the screen
    # 1) render the message
    the_text  = font.render(message, True, BLUE, (250,250,250))
    # 2) set it's location
    # [x, y, width, height]
    text_rect = [1, line*text_height+1, screen_width, text_height]
    # 3) blit it to the screen
    screen.blit(the_text, text_rect)

def abort_experiment():
    # this function called when user hits Esc:
    # asks: do you really want to quit?, etc.
    screen.fill((250,250,250))# GRAY)  # fill it with a middle gray...
    blit_text('Do you really want to quit? (y/n)',5)
    pygame.display.update()
    quit_response = get_keypress()
    if quit_response in ['y','Y']:
        # close the screen
        pygame.display.quit()
        # and quit
        sys.exit()
    else:
        # simply resume
        screen.fill((250,250,250))# GRAY)  # fill it with a middle gray...
        blit_text('Enter A category label (A or B) to continue',5)
        pygame.display.update()
    

def key_to_letter(key_val, key_mod=1):# mod=1 means upper-case; mod = 0 means lower-case
    # takes a key value as recorded by the event listner and returns the corresponding letter
    # a (and A) is key value 97; z (and Z) is key value 122
    #
    # first, conver the key value to the ASCII value: A = 65; Z is 90,
    #   so ASCII = key value minus 32
    if key_mod == 0: # lower case
        ascii = key_val
    elif key_mod == 1: # upper case
        ascii = key_val - 32
    else:
        print('error in key_to_letter: key_mod =', key_mod)
        # sys.exit()
        abort_experiment()
    if ascii < 256:
        # DIAG
        # print chr(ascii)
        return chr(ascii)
    else:
        # DIAG
        print('Error: Returning a space')
        
        return ' ' # return space is not a valid ascii value

def get_keypress(trigger=None):
    # this is my version
    # it waits for the user to enter a key in order to move on
    all_done = False
    while not all_done:
        event_list = pygame.event.get()
        for event in event_list:
            # process the_event according to what type of event it is
            if event.type == QUIT:
                # sys.exit()
                return key_to_letter(abort_experiment())
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # sys.exit(0)
                    abort_experiment()
                elif key_to_letter(event.key, event.mod) == trigger:
                    all_done = True
                elif trigger == None:
                    # if there's no trigger, then assume that the program
                    # wants to know what the user entered
                    all_done = True
                    return key_to_letter(event.key, event.mod)

# # (7) fill the screen with the background color and write dummy message
screen.fill(LIGHTGRAY)
blit_text("It's all up to you now. Write your code and delete me.",8)
blit_text("Hit any key to close this screen and move on with your life.",9)
pygame.display.update()

# # (8) wait for a keypress.
# get_keypress()

time.sleep(3)

# (9) close the screen and quit
pygame.display.quit()

