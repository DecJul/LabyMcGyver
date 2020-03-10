# -*- coding: utf8 -*-
import pygame
from pygame.locals import *

import random

"""Programme pour le Projet3 de la formation dev appli: Python"""


class Game:
    """Class qui gère les mécanisme du jeu"""
    ON = True
    RULE = True
    PLAY = False
    END = False
    
    def init():
        Laby.place_wall()
        Graphic.show_case(Image.RULE,Position(0,0))

    def event():
        for event in pygame.event.get():
            if event.type == QUIT:
                Game.off()
            if Game.RULE:
                Game.rule(event)
            elif Game.PLAY:
                McGyver.move(event)
                if McGyver.POS == Gardien.POS:
                    Game.end()
            elif Game.END:
                Game.replay(event)

    def rule(event):
        if event.type == KEYDOWN:
            print("test")
            Game.new_game()
            Game.RULE = False
          
    def new_game():
        Game.PLAY = True
        Game.END = False
        Laby.ITEMS = []
        McGyver.new_game()
        Graphic.create_laby()
        Laby.place_item("Aiguille")
        Laby.place_item("Tube")
        Laby.place_item("Ether")
        Graphic.new_item()
        Graphic.show_case(Image.MCGYVER_DOWN,McGyver.POS)
        Graphic.show_case(Image.GARDIEN,Gardien.POS)
                
    def new_case(position,file):
        item = Item("new_case",position)
        if item in Laby.WALLS or position.lat not in range(15) or position.lon not in range(15):
            Graphic.show_case(Image.SOL,McGyver.POS)
            Graphic.show_case(file,McGyver.POS)
        elif position == McGyver.POS:
            pass
        else:
            Graphic.show_case(Image.SOL,McGyver.POS)
            McGyver.POS = position
            Graphic.show_case(Image.SOL,McGyver.POS)
            Graphic.show_case(file,McGyver.POS)
            if item in Laby.ITEMS:
                Item.loot_item(position)
    
    def end():
        Game.END = True
        Game.PLAY = False
        if McGyver.SERINGUE == True:
            Graphic.show_case(Image.WIN,Position(5,1))
        else:
            Graphic.show_case(Image.LOOSE,Position(5,1))

    def replay(event):
        if event.type == KEYDOWN:
            Game.new_game()
                   
    def off():
        Game.ON = False


class Graphic:
    """Class qui s'occupe uniquement de la partie graphique du jeu"""
    WIDTH_CASE = 48
    HEIGTH_CASE = 48
    
    @classmethod
    def open(cls):
        cls.WINDOW = pygame.display.set_mode((Graphic.WIDTH_CASE*(Laby.LAT_MAX+1),Graphic.HEIGTH_CASE*(Laby.LON_MAX+2)))
    
    def create_laby():
        for i in range(Laby.LAT_MAX+1):
            for j in range(Laby.LON_MAX+1):
                wall = Wall(Position(j,i))
                if wall in Laby.WALLS:
                    Graphic.show_case(Image.WALL,wall.pos)
                else:
                    Graphic.show_case(Image.SOL,wall.pos)
        Graphic.show_case(Image.INTERFACE,Position(Laby.LON_MAX+1,0))

    def new_item():
        for i in Laby.ITEMS:
            Graphic.item(i.name, i.pos)
                
    def item(name,pos):
        if name == "Aiguille":
            Graphic.show_case(Image.AIGUILLE,pos)
        elif name == "Tube":
            Graphic.show_case(Image.TUBE,pos)
        elif name == "Ether":
            Graphic.show_case(Image.ETHER,pos)
    
    def show_case(file,position):
        Graphic.WINDOW.blit(file, (position.lon*Graphic.WIDTH_CASE,position.lat*Graphic.HEIGTH_CASE))
        
    def refresh():
        pygame.display.flip()


class Position:
    """Class qui gère les positions dans le labyrinthe de n'importe quel objet ou personnage"""
    def __init__(self, latitude, longitude):
        self.lat = latitude
        self.lon = longitude
        
    def __eq__(self, other):
        return (self.lat == other.lat) and (self.lon == other.lon)


class Laby:
    """Class qui stocke le placement des murs et des objet ainsi que les limites du labyrinthe"""
    LAT_MIN = 0
    LON_MIN = 0
    LAT_MAX = 14
    LON_MAX = 14
    WALLS = []
    ITEMS = []

    @classmethod
    def place_wall(cls):
        fichier = open("Map.txt", "r")
        contenu = fichier.read()
        fichier.close()
        map = contenu.split("\n")
        for i in range(cls.LAT_MAX+1):
            for j in range(cls.LON_MAX+1):
                if map[i][j]=='X':
                    position = Position(i,j)
                    wall = Wall(position)
                    cls.WALLS.append(wall)
                    
    @classmethod
    def place_item(cls,name):
        latitude = random.randint(cls.LAT_MIN,cls.LAT_MAX)
        longitude = random.randint(cls.LON_MIN,cls.LON_MAX)
        position = Position (latitude, longitude)
        item = Item(name, position)
        if item not in cls.ITEMS and item not in cls.WALLS and item.pos not in (McGyver.POS,Gardien.POS):
            cls.ITEMS.append(item)
        else:
            cls.place_item(name)


class Image:
    """Class pour charger toutes les images utilisé dans le jeu"""
    @classmethod
    def load (cls):
        cls.SOL = pygame.image.load("Ground.png").convert()
        cls.WALL = pygame.image.load("Wall.png").convert()
        cls.MCGYVER_UP = pygame.image.load("MacGyver_Up.png").convert_alpha()
        cls.MCGYVER_DOWN = pygame.image.load("MacGyver_Down.png").convert_alpha()
        cls.MCGYVER_LEFT = pygame.image.load("MacGyver_Left.png").convert_alpha()
        cls.MCGYVER_RIGHT = pygame.image.load("MacGyver_Right.png").convert_alpha()
        cls.GARDIEN = pygame.image.load("Gardien_Down.png").convert_alpha()
        cls.ETHER = pygame.image.load("Ether.png").convert_alpha()
        cls.AIGUILLE = pygame.image.load("Aiguille.png").convert_alpha()
        cls.TUBE = pygame.image.load("Tube.png").convert_alpha()
        cls.WIN = pygame.image.load("win.jpg").convert_alpha()
        cls.LOOSE = pygame.image.load("loose.jpg").convert_alpha()
        cls.RULE = pygame.image.load("rule.jpg").convert_alpha()
        cls.INTERFACE = pygame.image.load("Interface.jpg").convert_alpha()
        cls.SERINGUE = pygame.image.load("Seringue.jpg").convert_alpha()


class McGyver:
    """Class du personnage dirigé par le joueur"""
    @classmethod
    def new_game(cls):
        cls.POS = Position(0, 0)
        cls.SERINGUE = False
        cls.LOOT = 0
    
    @classmethod
    def craft_seringue(cls):
        cls.SERINGUE = True
        Graphic.show_case(Image.SERINGUE,Position(15,11))
            
    def move(event):
        if event.type == KEYDOWN:
            if event.key == K_DOWN or event.key == K_s:
                newpos = Position(McGyver.POS.lat+1,McGyver.POS.lon)
                file = Image.MCGYVER_DOWN
                Game.new_case(newpos,file)
            elif event.key == K_UP or event.key == K_w:
                newpos = Position(McGyver.POS.lat-1,McGyver.POS.lon)
                file = Image.MCGYVER_UP
                Game.new_case(newpos,file)
            elif event.key == K_LEFT or event.key == K_a:
                newpos = Position(McGyver.POS.lat,McGyver.POS.lon-1)
                file = Image.MCGYVER_LEFT
                Game.new_case(newpos,file)
            elif event.key == K_RIGHT or event.key == K_d:
                newpos = Position(McGyver.POS.lat,McGyver.POS.lon+1)
                file = Image.MCGYVER_RIGHT
                Game.new_case(newpos,file)


class Gardien:
    """Class pour géré le gardien"""
    POS = Position(14,14)


class Item:
    """Class pour géré les objets qui peuvent être ramassé par le joueur"""
    def __init__(self, name, position):
        self.pos = position
        self.name = name
        self.loot = False
        
    def __eq__(self, other):
        """Permet de comparer la position d'un objet à la position d'un autre objet ou d'un mur"""
        return (self.pos == other.pos)
                
    def loot_item(position):
        """Permet d'indiquer si un objet est récupéré et permet aussi de vérifier si tous les objets ont été récupéré"""
        for i in Laby.ITEMS:
            if i.pos == position and i.loot == False:
                i.loot = True
                Graphic.item(i.name,Position(15,1+(McGyver.LOOT*3)))
                McGyver.LOOT += 1
                if McGyver.LOOT == 3:
                    McGyver.craft_seringue()
                break


class Wall:
    """Class pour les murs"""
    def __init__(self, position):
        self.pos = position
        
    def __eq__(self, other):
        """Permet de comparer la position d'un mur à la position d'un autre mur ou d'un objet"""
        return (self.pos == other.pos)


def main():
    """Fonction principale en 2 temps:
    -on initialise toutes les données du jeu
    -puis on est dans une boucle qui continue tant que l'utilisateur ne quitte pas le jeu
    """
    pygame.init()
    Graphic.open()
    Image.load()
    Game.init()
    while Game.ON:
        Graphic.refresh()
        Game.event()


main()