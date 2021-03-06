#coding:utf-8
background_image_filename = '1.jpg'
sprite_image_filename = '2.jpg'

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

pygame.init()
screen = pygame.display.set_mode((1024,800),0,32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

clock = pygame.time.Clock()

position = Vector2(100.0,100.0)
heading = Vector2()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background,(0,0))
    screen.blit(sprite,(x,100))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    destination =  Vector2(*pygame.mouse.get_pos())-Vector2(*sprite.get_size())/2

    vector_to_mouse = Vector2.from_points(position,destination)

    vector_to_mouse.normalize()

    heading = heading+(vector_to_mouse * .6)
    position += heading * (time_passed_seconds)

    pygame.display.update()
