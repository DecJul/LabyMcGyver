"""Function for the graphism's aspect of the game"""
# -*- coding: utf8 -*-
import pygame

from module.object import *

WINDOW = ''

def open_window():
    """open the windows"""
    global WINDOW
    pygame.init()
    width = WIDTH_CASE * (LAT_MAX + 1)
    heigth = HEIGTH_CASE * (LON_MAX + 2)
    WINDOW = pygame.display.set_mode((width, heigth))

def create_laby():
    """Build the graphism's part of the labyrinthe after Laby.place_wall"""
    for i in range(LAT_MAX + 1):
        for j in range(LON_MAX + 1):
            wall = Wall(Position(j, i))
            if wall in Laby.WALLS:
                show_case(WALL, wall.pos)
            else:
                show_case(SOL, wall.pos)
    show_case(INTERFACE, Position(LON_MAX + 1, 0))

def new_item():
    """show all of the items on the map"""
    for i in Laby.ITEMS:
        item(i.name, i.pos)

def item(name, pos):
    """show one item with their name"""
    if name == "Aiguille":
        show_case(AIGUILLE, pos)
    elif name == "Tube":
        show_case(TUBE, pos)
    elif name == "Ether":
        show_case(ETHER, pos)

def show_case(file, position):
    """show the image with his position"""
    pos_lon = position.lon * WIDTH_CASE
    pos_lat = position.lat * HEIGTH_CASE
    WINDOW.blit(load_image(file), (pos_lon, pos_lat))

def load_image(file):
    """load image"""
    return pygame.image.load(file).convert_alpha()

def refresh():
    """refresh the graphism after each new turn of the game"""
    pygame.display.flip()
