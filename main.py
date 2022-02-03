import random

import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((1080, 960))

screen.fill((100,100, 100))
cloud_image



class Rain:

    def __init__(self):
        self.ypos = -1
        self.xpos = random.randint(1, 100)

    def draw(self):
        pygame.draw.circle(screen, (200,200,200), (self.xpos, self.ypos), 10)

    def Move(self):


RainDrops: []

ra










# clock = pygame.time.clock()

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        #     ypos += 1

    # pressedKeys = pygame.key.get_pressed()
    #
    # screen.fill((100,100, 100))
    # # circle
    # pygame.draw.circle(screen, (200,200,200), (xpos,ypos), 10)
    #
    # ypos += 10




    # Rectangle
    # pygame.draw.rect(screen, (50,50,50), (xpos,ypos,200,100))


# arrows
#     if pressedKeys[K_RIGHT]:
#         xpos += 1
#
#     if pressedKeys[K_LEFT]:
#         xpos -= 1
#
#     if pressedKeys[K_UP]:
#         ypos -= 1
#
#     if pressedKeys[K_DOWN]:
#         ypos += 1
# WASD
#     if pressedKeys[K_d]:
#         xpos += 1
#
#     if pressedKeys[K_a]:
#         xpos -= 1
#
#     if pressedKeys[K_w]:
#         ypos -= 1
#
#     if pressedKeys[K_s]:
#         ypos += 1

    pygame.display.flip()
