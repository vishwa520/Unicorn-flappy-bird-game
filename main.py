import random   #for generating random numbers
import sys# we will use sys.exit to exit the program
import pygame
import pygame.locals
import *  #basic pygame imports

#global variables for the game
FPS  = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = "/gallery/sprites/bird.png"
BACKGROUND = "/gallery/sprites/background.png"
PIPE = "/gallery/sprites/pipe.png"

if __name__ == "__main__":
    #This will be the main point from where our game starts
    pygame.init()  #initiallize all pygame's module
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Unicorn Flappy Bird by Vishwa")
    GAME_SPRITES['numbers'] = (
        pygame.image.load('/gallery/sprites/0.png').convert_alpha()
        pygame.image.load('/gallery/sprites/1.png').convert_alpha()
        pygame.image.load('/gallery/sprites/2.png').convert_alpha()
        pygame.image.load('/gallery/sprites/3.png').convert_alpha()
        pygame.image.load('/gallery/sprites/4.png').convert_alpha()
        pygame.image.load('/gallery/sprites/5.png').convert_alpha()
        pygame.image.load('/gallery/sprites/6.png').convert_alpha()
        pygame.image.load('/gallery/sprites/7.png').convert_alpha()
        pygame.image.load('/gallery/sprites/8.png').convert_alpha()
        pygame.image.load('/gallery/sprites/9.png').convert_alpha()
    )
    GAME_SPRITES['base'] = pygame.image.load('/gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
     pygame.image.load(PIPE).convert_alpha()
     )

# game sounds