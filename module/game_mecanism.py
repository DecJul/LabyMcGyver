"""Function for the game mecanism"""
# -*- coding: utf8 -*-
import pygame
from pygame.locals import *

from module.object import *
import module.graphism as Graphic


ON = True
RULE = True
PLAY = False
END = False

def init():
    """Build the labyrinthe and show the rules"""
    Laby.place_wall()
    Graphic.show_case(RULES, Position(0, 0))

def instruction():
    """collect the user's instructions and separate the phases of the game """
    for event in pygame.event.get():
        if event.type == QUIT:
            off()
        if RULE:
            rule(event)
        elif PLAY:
            move(event)
            if McGyver.POS == Gardien.POS:
                end()
        elif END:
            replay(event)

def rule(event):
    """the rule's phase before the beginning of the game"""
    global RULE
    if event.type == KEYDOWN:
        new_game()
        RULE = False

def new_game():
    """initialise or reinitialise the game's variables"""
    global PLAY, END
    PLAY = True
    END = False
    Laby.ITEMS = []
    McGyver.new_game()
    Graphic.create_laby()
    Laby.place_item("Aiguille")
    Laby.place_item("Tube")
    Laby.place_item("Ether")
    Graphic.new_item()
    Graphic.show_case(MCGYVER_DOWN, McGyver.POS)
    Graphic.show_case(GARDIEN, Gardien.POS)

def new_case(position, file):
    """Analyse the future's position of the player and decide if he can move on"""
    item = Item("new_case", position)
    if item in Laby.WALLS or position.lat not in range(15) or position.lon not in range(15):
        Graphic.show_case(SOL, McGyver.POS)
        Graphic.show_case(file, McGyver.POS)
    elif position == McGyver.POS:
        pass
    else:
        Graphic.show_case(SOL, McGyver.POS)
        McGyver.POS = position
        Graphic.show_case(SOL, McGyver.POS)
        Graphic.show_case(file, McGyver.POS)
        if item in Laby.ITEMS:
            loot_item(position)

def end():
    """when the player reach the guardian, show if he win and activate the end' phase"""
    global END, PLAY
    END = True
    PLAY = False
    if McGyver.SERINGUE:
        Graphic.show_case(WIN, Position(5, 1))
    else:
        Graphic.show_case(LOOSE, Position(5, 1))

def replay(event):
    """end phase, the player can play a new game"""
    if event.type == KEYDOWN:
        new_game()

def off():
    """use when we want leave the game"""
    global ON
    ON = False

def move(event):
    """play phase, we analyse the move decide by the player"""
    if event.type == KEYDOWN:
        if event.key == K_DOWN or event.key == K_s:
            newpos = Position(McGyver.POS.lat+1, McGyver.POS.lon)
            file = MCGYVER_DOWN
            new_case(newpos, file)
        elif event.key == K_UP or event.key == K_w:
            newpos = Position(McGyver.POS.lat-1, McGyver.POS.lon)
            file = MCGYVER_UP
            new_case(newpos, file)
        elif event.key == K_LEFT or event.key == K_a:
            newpos = Position(McGyver.POS.lat, McGyver.POS.lon-1)
            file = MCGYVER_LEFT
            new_case(newpos, file)
        elif event.key == K_RIGHT or event.key == K_d:
            newpos = Position(McGyver.POS.lat, McGyver.POS.lon+1)
            file = MCGYVER_RIGHT
            new_case(newpos, file)

def loot_item(position):
    """Check if an item is loot and if all item are loot"""
    for i in Laby.ITEMS:
        if i.pos == position and not i.loot:
            i.loot = True
            Graphic.item(i.name, Position(15, 1 + (McGyver.LOOT*3)))
            McGyver.LOOT += 1
            if McGyver.LOOT == 3:
                craft_seringue()
            break

def craft_seringue():
    """use when all item are loot"""
    McGyver.SERINGUE = True
    Graphic.show_case(SERINGUE, Position(15, 11))
