from pygame import *
import pygame
import sys

pygame.init()

screen = display.set_mode((600,600))

display.set_caption("Snakes & Ladders")

bg = image.load("redwins.png")
bg = transform.scale(bg,(600,600))
icon = image.load("icon.png")
display.set_icon(icon)

display.update()
while True:
    screen.blit(bg,(0,0))
    for e in event.get():
        if e.type == QUIT:
            quit();
            sys.exit()

    display.update()